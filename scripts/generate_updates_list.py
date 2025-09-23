#!/usr/bin/env python3
"""
Script to automatically generate a list of all updates with their H1 titles as clickable links.
This script extracts H1 titles from all update markdown files and generates markdown list format.
"""

import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime

def load_category_config(updates_dir):
    """Load category configuration from categories.yml file."""
    config_file = updates_dir / 'categories.yml'
    category_ratings = {}
    
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if data and 'categories' in data:
                for category_name, category_data in data['categories'].items():
                    if isinstance(category_data, dict) and 'rating' in category_data:
                        category_ratings[category_name] = category_data['rating']
                    elif isinstance(category_data, (int, float)):
                        # Handle simple format: category_name: rating
                        category_ratings[category_name] = int(category_data)
        except yaml.YAMLError as e:
            print(f"Error parsing categories.yml: {e}")
        except Exception as e:
            print(f"Error reading categories.yml: {e}")
    
    return category_ratings

def update_categories_file(updates_dir, discovered_categories, default_rating=10):
    """Update categories.yml file with newly discovered categories."""
    config_file = updates_dir / 'categories.yml'
    
    # Load existing categories
    existing_categories = load_category_config(updates_dir)
    
    # Find new categories that aren't in the config
    new_categories = []
    for category in discovered_categories:
        if category and category not in existing_categories:
            new_categories.append(category)
    
    if not new_categories:
        return False  # No updates needed
    
    # Load existing YAML data
    data = {'categories': {}}
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {'categories': {}}
        except Exception as e:
            print(f"Warning: Could not load existing categories.yml: {e}")
            data = {'categories': {}}
    
    # Ensure categories key exists
    if 'categories' not in data:
        data['categories'] = {}
    
    # Add new categories
    for category in sorted(new_categories):
        data['categories'][category] = {
            'rating': default_rating,
            'description': f"Auto-added category"
        }
    
    # Write updated YAML
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, 
                     allow_unicode=True, width=1000)
        
        print(f"✅ Added {len(new_categories)} new categories to categories.yml: {', '.join(new_categories)}")
        return True
    except Exception as e:
        print(f"Error writing categories.yml: {e}")
        return False

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

def extract_date_title_and_category(file_path):
    """Extract date and category from frontmatter and H1 title from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter (between --- and ---)
        frontmatter_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        date = None
        category = None
        draft = False
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # Extract date from frontmatter
            date_match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', frontmatter, re.MULTILINE)
            if date_match:
                date = date_match.group(1)
            
            # Extract category from frontmatter
            category_match = re.search(r'^category:\s*"([^"]*)"', frontmatter, re.MULTILINE)
            if category_match:
                category = category_match.group(1)
            
            # Extract draft status from frontmatter
            draft_match = re.search(r'^draft:\s*(true|false)', frontmatter, re.MULTILINE)
            if draft_match:
                draft = draft_match.group(1).lower() == 'true'
        
        # Skip if draft is true
        if draft:
            return None, None, None, True  # Return None for date/title/category and True for is_draft
        
        # Find the first H1 title (line starting with # followed by space)
        lines = content.split('\n')
        title = None
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                # Remove the # and leading space, return the title
                title = line[2:].strip()
                break
        
        return date, title, category, False  # Return False for is_draft
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None, None, False

def format_date(date_str):
    """Format date string from YYYY-MM-DD to 'MMM DD, YYYY' format."""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%b %d, %Y')
    except ValueError:
        return date_str

def get_update_files_info(updates_dir):
    """Get information about all update files including dates, titles, and categories."""
    if not updates_dir.exists():
        return []
    
    update_files = []
    for file_path in updates_dir.glob("*.md"):
        if file_path.name == "index.md":
            continue  # Skip index.md
        
        date, title, category, is_draft = extract_date_title_and_category(file_path)
        if is_draft:
            # Skip draft files
            continue
        if title:
            formatted_date = format_date(date) if date else "Unknown Date"
            update_files.append({
                'filename': file_path.name,
                'title': title,
                'date': formatted_date,
                'raw_date': date,
                'category': category,
                'path': file_path
            })
    
    return update_files

def generate_updates_list_for_product(product_name):
    """Generate updates list for a specific product, grouped by categories and sorted by centralized rating."""
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
    
    # Collect all discovered categories
    discovered_categories = set()
    for update in update_files:
        if update['category']:
            discovered_categories.add(update['category'])
    
    # Update .categories file with new categories
    update_categories_file(updates_dir, discovered_categories)
    
    # Load centralized category configuration (after potential update)
    category_ratings = load_category_config(updates_dir)
    
    # Sort by raw date in descending order (newest first)
    update_files.sort(key=lambda x: x['raw_date'] or '', reverse=True)
    
    # Group updates by category (posts without category default to "Updates")
    categorized_updates = {}
    
    for update in update_files:
        category = update['category'] or "Updates"  # Default to "Updates" if no category
        
        if category not in categorized_updates:
            categorized_updates[category] = []
        categorized_updates[category].append(update)
    
    # Generate markdown list grouped by categories, sorted by centralized rating (highest first)
    markdown_sections = []
    
    # Sort categories by centralized rating in descending order (highest rating first)
    sorted_categories = sorted(categorized_updates.keys(), 
                              key=lambda cat: category_ratings.get(cat, 0), 
                              reverse=True)
    
    # Add categorized sections (sorted by centralized rating)
    for category in sorted_categories:
        markdown_sections.append(f"## {category}")
        markdown_sections.append("")  # Empty line after section header
        
        for update in categorized_updates[category]:
            filename = update['filename']
            title = update['title']
            raw_date = update['raw_date'] or "Unknown Date"
            markdown_sections.append(f"- {raw_date}: [{title}]({filename})")
        
        markdown_sections.append("")  # Empty line after section
    
    return '\n'.join(markdown_sections), f"Generated list for {product_name} with {len(update_files)} updates"

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
    
    # Create the standardized content with category support
    variable_name = f"{product_name}_updates"
    content = f"""# Updates & Events

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
    content = f"""# Updates & Events

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
