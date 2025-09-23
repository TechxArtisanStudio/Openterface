#!/usr/bin/env python3
"""
Script to count update posts and YouTube links in all product folders and update mkdocs.yml
with the total count for each product for use in templates.
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
    # Get the project root directory (assuming script is in scripts/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
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

def count_youtube_links_for_product(product_name):
    """Count the number of YouTube links in a product's .youtube.list file."""
    # Get the project root directory (assuming script is in scripts/)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Path to the .youtube.list file for this product
    youtube_list_path = project_root / "docs" / "product" / product_name / "reviews" / ".youtube.list"
    
    if not youtube_list_path.exists():
        return 0, []
    
    # Count non-empty lines in the .youtube.list file
    youtube_links = []
    try:
        with open(youtube_list_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):  # Skip empty lines and comments
                    youtube_links.append(line)
    except Exception as e:
        print(f"Error reading {youtube_list_path}: {e}")
        return 0, []
    
    return len(youtube_links), youtube_links

def get_all_product_folders():
    """Get all product folder names from the product directory."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
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

def update_mkdocs_yml(product_counts, youtube_counts):
    """Update the mkdocs.yml file with variables for each product's update and YouTube counts."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    mkdocs_path = project_root / "mkdocs.yml"
    
    if not mkdocs_path.exists():
        print(f"Error: mkdocs.yml not found at {mkdocs_path}")
        return False
    
    # Read the current mkdocs.yml content
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process each product's update count
    for product_name, count in product_counts.items():
        variable_name = f"{product_name}_updates"
        
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
    
    # Process each product's YouTube count
    for product_name, count in youtube_counts.items():
        variable_name = f"{product_name}_youtube"
        
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
    """Main function to count updates and YouTube links for all products and update mkdocs.yml."""
    print("Scanning all product folders for updates directories and YouTube lists...")
    
    # Get all product folders
    product_folders = get_all_product_folders()
    
    if not product_folders:
        print("No product folders found.")
        return
    
    print(f"Found product folders: {', '.join(product_folders)}")
    
    # Count updates for each product
    product_counts = {}
    youtube_counts = {}
    total_updates = 0
    total_youtube = 0
    
    for product_name in product_folders:
        # Count update posts
        count, update_files = count_update_posts_for_product(product_name)
        product_counts[product_name] = count
        total_updates += count
        
        if count > 0:
            print(f"\n{product_name}: Found {count} update posts:")
            for file_name in sorted(update_files):
                print(f"  - {file_name}")
        else:
            print(f"\n{product_name}: No updates directory found")
        
        # Count YouTube links
        youtube_count, youtube_links = count_youtube_links_for_product(product_name)
        youtube_counts[product_name] = youtube_count
        total_youtube += youtube_count
        
        if youtube_count > 0:
            print(f"\n{product_name}: Found {youtube_count} YouTube links:")
            for link in sorted(youtube_links):
                print(f"  - {link}")
        else:
            print(f"\n{product_name}: No .youtube.list file found")
    
    print(f"\nTotal updates across all products: {total_updates}")
    print(f"Total YouTube links across all products: {total_youtube}")
    
    # Show what variables will be created/updated
    print(f"\nVariables to be created/updated in mkdocs.yml:")
    for product_name, count in product_counts.items():
        variable_name = f"{product_name}_updates"
        print(f"  - {variable_name}: {count}")
    
    for product_name, count in youtube_counts.items():
        if count > 0:  # Only show products that have YouTube links
            variable_name = f"{product_name}_youtube"
            print(f"  - {variable_name}: {count}")
    
    print("\nUpdating mkdocs.yml...")
    if update_mkdocs_yml(product_counts, youtube_counts):
        print("✅ Successfully updated mkdocs.yml with product update and YouTube variables")
        print("   You can now use these variables in your templates:")
        for product_name in product_counts.keys():
            variable_name = f"{product_name}_updates"
            print(f"   - {{ config.extra.{variable_name} }}")
        for product_name in youtube_counts.keys():
            if youtube_counts[product_name] > 0:
                variable_name = f"{product_name}_youtube"
                print(f"   - {{ config.extra.{variable_name} }}")
    else:
        print("❌ Failed to update mkdocs.yml")
        sys.exit(1)

if __name__ == "__main__":
    main()
