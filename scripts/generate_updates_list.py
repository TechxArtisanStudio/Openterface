#!/usr/bin/env python3
"""
Script to automatically generate a list of all updates with their H1 titles as clickable links.
This script extracts H1 titles from all update markdown files and generates markdown list format.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

def extract_h1_title(file_path):
    """Extract H1 title from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the first H1 title (line starting with # followed by space)
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                # Remove the # and leading space, return the title
                return line[2:].strip()
        
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def get_update_files_info(updates_dir):
    """Get information about all update files including H1 titles."""
    if not updates_dir.exists():
        return []
    
    update_files = []
    for file_path in updates_dir.glob("*.md"):
        if file_path.name == "index.md":
            continue  # Skip index.md
        
        h1_title = extract_h1_title(file_path)
        if h1_title:
            update_files.append({
                'filename': file_path.name,
                'title': h1_title,
                'path': file_path
            })
    
    return update_files

def generate_updates_list_for_product(product_name):
    """Generate updates list for a specific product."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Path to the updates directory for this product
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    
    if not updates_dir.exists():
        return None, f"No updates directory found for {product_name}"
    
    update_files = get_update_files_info(updates_dir)
    
    if not update_files:
        # Return empty list if no update files found
        return "", f"No update files found for {product_name}, created empty index"
    
    # Sort by filename (which contains dates) in descending order
    update_files.sort(key=lambda x: x['filename'], reverse=True)
    
    # Generate markdown list
    markdown_lines = []
    for update in update_files:
        filename = update['filename']
        title = update['title']
        # Create clickable link: [title](filename)
        markdown_lines.append(f"- [{title}]({filename})")
    
    return '\n'.join(markdown_lines), f"Generated list for {product_name} with {len(update_files)} updates"

def generate_all_products_updates_list():
    """Generate updates lists for all products."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    product_dir = project_root / "docs" / "product"
    
    if not product_dir.exists():
        print(f"Error: Product directory not found at {product_dir}")
        return {}
    
    # Get all subdirectories in the product folder
    product_folders = []
    for item in product_dir.iterdir():
        if item.is_dir():
            product_folders.append(item.name)
    
    results = {}
    for product_name in sorted(product_folders):
        markdown_list, message = generate_updates_list_for_product(product_name)
        if markdown_list is not None:  # Changed condition to handle empty strings
            results[product_name] = {
                'markdown': markdown_list,
                'message': message
            }
        else:
            # Create empty index for products without updates directory
            results[product_name] = {
                'markdown': "",
                'message': f"Created empty updates index for {product_name}"
            }
    
    return results

def create_or_update_index_file(product_name, markdown_list):
    """Create or update the index.md file for a specific product with the standardized format."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    index_path = updates_dir / "index.md"
    
    # Create the updates directory if it doesn't exist
    updates_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the standardized content
    variable_name = f"{product_name}_updates"
    content = f"""# Updates

**Total Updates: {{{{ config.extra.{variable_name} }}}}**

{markdown_list}
"""
    
    # Write the content to index.md (overwrite if exists)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def create_empty_updates_index(product_name):
    """Create an empty updates index for products without updates directory."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    index_path = updates_dir / "index.md"
    
    # Create the updates directory
    updates_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the standardized content with empty list
    variable_name = f"{product_name}_updates"
    content = f"""# Updates

**Total Updates: {{{{ config.extra.{variable_name} }}}}**

"""
    
    # Write the content to index.md
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Main function to generate and optionally update update lists."""
    parser = argparse.ArgumentParser(description='Generate automatic updates list from H1 titles')
    parser.add_argument('--product', help='Generate list for specific product only')
    parser.add_argument('--update-files', action='store_true', 
                       help='Update the index.md files with generated lists')
    parser.add_argument('--output', help='Output file to save generated lists')
    
    args = parser.parse_args()
    
    if args.product:
        # Generate for specific product
        markdown_list, message = generate_updates_list_for_product(args.product)
        if markdown_list:
            print(f"✅ {message}")
            print("\nGenerated markdown list:")
            print(markdown_list)
            
            if args.update_files:
                if create_or_update_index_file(args.product, markdown_list):
                    print(f"✅ Updated {args.product}/updates/index.md")
                else:
                    print(f"❌ Failed to update {args.product}/updates/index.md")
        else:
            print(f"❌ {message}")
    else:
        # Generate for all products
        results = generate_all_products_updates_list()
        
        if not results:
            print("No products with updates found.")
            return
        
        print("Generated updates lists for all products:")
        for product_name, result in results.items():
            print(f"\n✅ {result['message']}")
            print(f"📝 {product_name} updates list:")
            print(result['markdown'])
            
            if args.update_files:
                if create_or_update_index_file(product_name, result['markdown']):
                    print(f"✅ Updated {product_name}/updates/index.md")
                else:
                    print(f"❌ Failed to update {product_name}/updates/index.md")
        
        # Save to output file if specified
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write("# Auto-generated Updates Lists\n\n")
                for product_name, result in results.items():
                    f.write(f"## {product_name}\n\n")
                    f.write(result['markdown'])
                    f.write("\n\n")
            print(f"\n💾 Saved all lists to {args.output}")

if __name__ == "__main__":
    import argparse
    main()
