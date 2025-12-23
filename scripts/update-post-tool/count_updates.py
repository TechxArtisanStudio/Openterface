#!/usr/bin/env python3
"""
Script to count update posts in all product, event, and app folders and update mkdocs.yml with the
total count for each product, event, and app for use in templates.
"""

import os
import re
import sys
from pathlib import Path

def is_draft_post(file_path):
    """Check if a markdown file is marked as draft in its frontmatter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter (between --- and ---)
        frontmatter_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # Extract draft status from frontmatter
            draft_match = re.search(r'^draft:\s*(true|false)', frontmatter, re.MULTILINE)
            if draft_match:
                return draft_match.group(1).lower() == 'true'
        
        return False  # Not a draft if no draft field is found
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def count_update_posts_for_product(product_name):
    """Count the number of update markdown files in a product's updates directory (English only)."""
    # Get the project root directory (script is in scripts/update-post-tool/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # Path to the updates directory for this product
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    
    if not updates_dir.exists():
        return 0, []
    
    # Count markdown files, excluding index files, translated files, and draft posts
    update_files = []
    for file_path in updates_dir.glob("*.md"):
        # Skip index files (both index.md and index.lang.md)
        if file_path.name == "index.md" or file_path.name.startswith("index."):
            continue
        
        # Skip translated files (files ending with .lang.md)
        if any(file_path.name.endswith(f".{lang}.md") for lang in ["zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]):
            continue
        
        # Skip draft posts
        if not is_draft_post(file_path):
            update_files.append(file_path.name)
    
    return len(update_files), update_files

def count_update_posts_for_event(event_name):
    """Count the number of update markdown files in an event's updates directory (English only)."""
    # Get the project root directory (script is in scripts/update-post-tool/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # Path to the updates directory for this event
    updates_dir = project_root / "docs" / "event" / event_name / "updates"
    
    if not updates_dir.exists():
        return 0, []
    
    # Count markdown files, excluding index files, translated files, and draft posts
    update_files = []
    for file_path in updates_dir.glob("*.md"):
        # Skip index files (both index.md and index.lang.md)
        if file_path.name == "index.md" or file_path.name.startswith("index."):
            continue
        
        # Skip translated files (files ending with .lang.md)
        if any(file_path.name.endswith(f".{lang}.md") for lang in ["zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]):
            continue
        
        # Skip draft posts
        if not is_draft_post(file_path):
            update_files.append(file_path.name)
    
    return len(update_files), update_files

def count_update_posts_for_app():
    """Count the number of update markdown files in the app's updates directory (English only)."""
    # Get the project root directory (script is in scripts/update-post-tool/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # Path to the updates directory for app
    updates_dir = project_root / "docs" / "app" / "updates"
    
    if not updates_dir.exists():
        return 0, []
    
    # Count markdown files, excluding index files, translated files, and draft posts
    update_files = []
    for file_path in updates_dir.glob("*.md"):
        # Skip index files (both index.md and index.lang.md)
        if file_path.name == "index.md" or file_path.name.startswith("index."):
            continue
        
        # Skip translated files (files ending with .lang.md)
        if any(file_path.name.endswith(f".{lang}.md") for lang in ["zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]):
            continue
        
        # Skip draft posts
        if not is_draft_post(file_path):
            update_files.append(file_path.name)
    
    return len(update_files), update_files

def get_all_product_folders():
    """Get all product folder names from the product directory."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    product_dir = project_root / "docs" / "product"
    
    if not product_dir.exists():
        print(f"Error: Product directory not found at {product_dir}")
        return []
    
    # Get all subdirectories in the product folder
    product_folders = []
    for item in product_dir.iterdir():
        if item.is_dir():
            product_folders.append(item.name)
    
    return sorted(product_folders)

def get_all_event_folders():
    """Get all event folder names from the event directory."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    event_dir = project_root / "docs" / "event"
    
    if not event_dir.exists():
        print(f"Error: Event directory not found at {event_dir}")
        return []
    
    # Get all subdirectories in the event folder
    event_folders = []
    for item in event_dir.iterdir():
        if item.is_dir():
            event_folders.append(item.name)
    
    return sorted(event_folders)

def update_mkdocs_yml(all_counts):
    """Update the mkdocs.yml file with variables for each product's and event's update counts."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    mkdocs_path = project_root / "mkdocs.yml"
    
    if not mkdocs_path.exists():
        print(f"Error: mkdocs.yml not found at {mkdocs_path}")
        return False
    
    # Read the current mkdocs.yml content
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process each item's update count (products and events)
    for item_name, count in all_counts.items():
        variable_name = f"{item_name}_updates"
        
        # Check if variable already exists in extra section
        if f'{variable_name}:' in content:
            # Update existing variable value
            pattern = rf'({variable_name}:\s*)\d+'
            replacement = f'\\g<1>{count}'
            content = re.sub(pattern, replacement, content)
        else:
            # Add variable to the extra section
            # Find the extra section and add the variable
            extra_pattern = r'(extra:\s*\n)'
            if re.search(extra_pattern, content):
                # Add after the first line of extra section
                replacement = f'\\g<1>  {variable_name}: {count}\n'
                content = re.sub(extra_pattern, replacement, content)
            else:
                print(f"Error: Could not find 'extra:' section in mkdocs.yml")
                return False
    
    # Write the updated content back to the file
    with open(mkdocs_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Main function to count updates for all products, events, and app and update mkdocs.yml."""
    print("Scanning all product, event, and app folders for updates directories...")
    
    # Get all product folders
    product_folders = get_all_product_folders()
    
    # Get all event folders
    event_folders = get_all_event_folders()
    
    if not product_folders and not event_folders:
        print("No product or event folders found.")
    
    if product_folders:
        print(f"Found product folders: {', '.join(product_folders)}")
    if event_folders:
        print(f"Found event folders: {', '.join(event_folders)}")
    
    # Count updates for each product
    all_counts = {}
    total_updates = 0
    
    if product_folders:
        print("\n--- Processing Products ---")
        for product_name in product_folders:
            # Count update posts
            count, update_files = count_update_posts_for_product(product_name)
            all_counts[product_name] = count
            total_updates += count
            
            if count > 0:
                print(f"\n{product_name}: Found {count} update posts:")
                for file_name in sorted(update_files):
                    print(f"  - {file_name}")
            else:
                print(f"\n{product_name}: No updates directory found")
    
    # Count updates for each event
    if event_folders:
        print("\n--- Processing Events ---")
        for event_name in event_folders:
            # Count update posts
            count, update_files = count_update_posts_for_event(event_name)
            all_counts[event_name] = count
            total_updates += count
            
            if count > 0:
                print(f"\n{event_name}: Found {count} update posts:")
                for file_name in sorted(update_files):
                    print(f"  - {file_name}")
            else:
                print(f"\n{event_name}: No updates directory found")
    
    # Count updates for app
    print("\n--- Processing App ---")
    count, update_files = count_update_posts_for_app()
    all_counts["app"] = count
    total_updates += count
    
    if count > 0:
        print(f"\napp: Found {count} update posts:")
        for file_name in sorted(update_files):
            print(f"  - {file_name}")
    else:
        print(f"\napp: No updates directory found")
    
    print(f"\nTotal updates across all products, events, and app: {total_updates}")
    
    # Show what variables will be created/updated
    print(f"\nVariables to be created/updated in mkdocs.yml:")
    for item_name, count in all_counts.items():
        variable_name = f"{item_name}_updates"
        print(f"  - {variable_name}: {count}")
    
    print("\nUpdating mkdocs.yml...")
    if update_mkdocs_yml(all_counts):
        print("✅ Successfully updated mkdocs.yml with product, event, and app update variables")
        print("   You can now use these variables in your templates:")
        for item_name in all_counts.keys():
            variable_name = f"{item_name}_updates"
            print(f"   - {{ config.extra.{variable_name} }}")
    else:
        print("❌ Failed to update mkdocs.yml")
        sys.exit(1)

if __name__ == "__main__":
    main()
