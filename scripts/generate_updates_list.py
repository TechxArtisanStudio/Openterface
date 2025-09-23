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
import argparse

def load_language_config():
    """Load language configuration from i18n.yml file."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    i18n_config_file = project_root / "i18n-tools" / "i18n.yml"
    
    default_language = "en"
    supported_languages = ["en"]
    
    if i18n_config_file.exists():
        try:
            with open(i18n_config_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if data:
                default_language = data.get('default_language', 'en')
                supported_languages = data.get('languages', ['en'])
        except yaml.YAMLError as e:
            print(f"Error parsing i18n.yml: {e}")
        except Exception as e:
            print(f"Error reading i18n.yml: {e}")
    
    return default_language, supported_languages

def load_category_config(updates_dir):
    """Load category configuration from categories.yml file."""
    config_file = updates_dir / 'categories.yml'
    category_ratings = {}
    category_translations = {}
    
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if data and 'categories' in data:
                for category_name, category_data in data['categories'].items():
                    if isinstance(category_data, dict):
                        if 'rating' in category_data:
                            category_ratings[category_name] = category_data['rating']
                        if 'translations' in category_data:
                            category_translations[category_name] = category_data['translations']
                    elif isinstance(category_data, (int, float)):
                        # Handle simple format: category_name: rating
                        category_ratings[category_name] = int(category_data)
        except yaml.YAMLError as e:
            print(f"Error parsing categories.yml: {e}")
        except Exception as e:
            print(f"Error reading categories.yml: {e}")
    
    return category_ratings, category_translations

def find_translated_file(base_filename, language, updates_dir):
    """Find translated version of a file for a specific language."""
    if language == "en":
        # English is the base language
        return updates_dir / base_filename
    
    # Try different naming patterns for translated files
    base_name = base_filename.replace('.md', '')
    patterns = [
        f"{base_name}.{language}.md",  # 240430-launch-announcement.zh.md
        f"{base_name}-{language}.md",  # 240430-launch-announcement-zh.md
    ]
    
    for pattern in patterns:
        translated_file = updates_dir / pattern
        if translated_file.exists():
            return translated_file
    
    # Fallback to English version
    return updates_dir / base_filename

def update_categories_file(updates_dir, discovered_categories, default_rating=10):
    """Update categories.yml file with newly discovered categories."""
    config_file = updates_dir / 'categories.yml'
    
    # Load existing categories
    existing_categories, _ = load_category_config(updates_dir)
    
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

def get_update_files_info(updates_dir, language="en"):
    """Get information about all update files including dates, titles, and categories for a specific language with fallback to English."""
    if not updates_dir.exists():
        return []
    
    update_files = []
    processed_base_files = set()  # Track which base files we've processed
    
    # First, collect all base English files
    english_files = {}
    for file_path in updates_dir.glob("*.md"):
        if file_path.name == "index.md" or file_path.name.startswith("index."):
            continue  # Skip index files
        
        # Skip translated files when collecting English files
        if any(file_path.name.endswith(f".{lang}.md") for lang in ["zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]):
            continue
        
        date, title, category, is_draft = extract_date_title_and_category(file_path)
        if is_draft:
            continue
        if title:
            # Store English file info keyed by base filename
            english_files[file_path.name] = {
                'filename': file_path.name,
                'title': title,
                'date': format_date(date) if date else "Unknown Date",
                'raw_date': date,
                'category': category,
                'path': file_path
            }
    
    if language == "en":
        # For English, return all English files
        return list(english_files.values())
    
    # For other languages, look for translated files first, then fallback to English
    for file_path in updates_dir.glob("*.md"):
        if file_path.name == "index.md" or file_path.name.startswith("index."):
            continue  # Skip index files
        
        # Check if this is a translated file for our target language
        if file_path.name.endswith(f".{language}.md"):
            # This is a translated file
            date, title, category, is_draft = extract_date_title_and_category(file_path)
            if is_draft:
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
                # Mark the base file as processed
                base_filename = file_path.name.replace(f".{language}.md", ".md")
                processed_base_files.add(base_filename)
    
    # Add English files as fallbacks for missing translations
    for base_filename, english_info in english_files.items():
        if base_filename not in processed_base_files:
            # This English file doesn't have a translation, use it as fallback
            update_files.append(english_info)
    
    return update_files

def generate_updates_list_for_product_and_language(product_name, language="en"):
    """Generate updates list for a specific product and language, grouped by categories and sorted by centralized rating."""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Path to the updates directory for this product
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    
    if not updates_dir.exists():
        return None, f"No updates directory found for {product_name}"
    
    update_files = get_update_files_info(updates_dir, language)
    
    if not update_files:
        # Return empty list if no update files found
        return "", f"No update files found for {product_name} in {language}, created empty index"
    
    # Collect all discovered categories
    discovered_categories = set()
    for update in update_files:
        if update['category']:
            discovered_categories.add(update['category'])
    
    # Update .categories file with new categories
    update_categories_file(updates_dir, discovered_categories)
    
    # Load centralized category configuration (after potential update)
    category_ratings, category_translations = load_category_config(updates_dir)
    
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
        # Get translated category name
        translated_category = category
        if category in category_translations and language in category_translations[category]:
            translated_category = category_translations[category][language]
        
        markdown_sections.append(f"## {translated_category}")
        markdown_sections.append("")  # Empty line after section header
        
        for update in categorized_updates[category]:
            filename = update['filename']
            title = update['title']
            raw_date = update['raw_date'] or "Unknown Date"
            markdown_sections.append(f"- {raw_date}: [{title}]({filename})")
        
        markdown_sections.append("")  # Empty line after section
    
    return '\n'.join(markdown_sections), f"Generated list for {product_name} in {language} with {len(update_files)} updates"

def generate_updates_list_for_product(product_name):
    """Generate updates list for a specific product, grouped by categories and sorted by centralized rating."""
    return generate_updates_list_for_product_and_language(product_name, "en")

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

def generate_all_products_updates_list_for_language(language):
    """Generate updates lists for all products in a specific language."""
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
        markdown_list, message = generate_updates_list_for_product_and_language(product_name, language)
        if markdown_list is not None:  # Changed condition to handle empty strings
            results[product_name] = {
                'markdown': markdown_list,
                'message': message
            }
        else:
            # Create empty index for products without updates directory
            results[product_name] = {
                'markdown': "",
                'message': f"Created empty updates index for {product_name} in {language}"
            }
    
    return results

def create_or_update_index_file(product_name, markdown_list, language="en"):
    """Create or update the index file for a specific product and language with the standardized format."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    
    # Determine the index filename based on language
    if language == "en":
        index_filename = "index.md"
    else:
        index_filename = f"index.{language}.md"
    
    index_path = updates_dir / index_filename
    
    # Create the updates directory if it doesn't exist
    updates_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the standardized content with category support
    variable_name = f"{product_name}_updates"
    content = f"""# Updates & Events

**Total Updates: {{{{ config.extra.{variable_name} }}}}**

{markdown_list}
"""
    
    # Write the content to index file (overwrite if exists)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def create_empty_updates_index(product_name, language="en"):
    """Create an empty updates index for products without updates directory."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    updates_dir = project_root / "docs" / "product" / product_name / "updates"
    
    # Determine the index filename based on language
    if language == "en":
        index_filename = "index.md"
    else:
        index_filename = f"index.{language}.md"
    
    index_path = updates_dir / index_filename
    
    # Create the updates directory
    updates_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the standardized content with empty list
    variable_name = f"{product_name}_updates"
    content = f"""# Updates & Events

**Total Updates: {{{{ config.extra.{variable_name} }}}}**

"""
    
    # Write the content to index file
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Main function to generate and optionally update update lists."""
    parser = argparse.ArgumentParser(description='Generate automatic updates list from H1 titles')
    parser.add_argument('--product', help='Generate list for specific product only')
    parser.add_argument('--language', help='Generate list for specific language only (default: en)')
    parser.add_argument('--all-languages', action='store_true', 
                       help='Generate lists for all supported languages')
    parser.add_argument('--update-files', action='store_true', 
                       help='Update the index files with generated lists')
    parser.add_argument('--output', help='Output file to save generated lists')
    
    args = parser.parse_args()
    
    # Load language configuration
    default_language, supported_languages = load_language_config()
    
    if args.all_languages:
        # Generate for all languages
        for language in supported_languages:
            print(f"\n🌍 Generating updates lists for language: {language}")
            
            if args.product:
                # Generate for specific product and language
                markdown_list, message = generate_updates_list_for_product_and_language(args.product, language)
                print(f"✅ {message}")
                if markdown_list:
                    print(f"\nGenerated markdown list for {language}:")
                    print(markdown_list)
                
                if args.update_files:
                    if create_or_update_index_file(args.product, markdown_list, language):
                        if language == "en":
                            print(f"✅ Updated {args.product}/updates/index.md")
                        else:
                            print(f"✅ Updated {args.product}/updates/index.{language}.md")
                    else:
                        if language == "en":
                            print(f"❌ Failed to update {args.product}/updates/index.md")
                        else:
                            print(f"❌ Failed to update {args.product}/updates/index.{language}.md")
            else:
                # Generate for all products and language
                results = generate_all_products_updates_list_for_language(language)
                
                if not results:
                    print(f"No products with updates found for {language}.")
                    continue
                
                print(f"Generated updates lists for all products in {language}:")
                for product_name, result in results.items():
                    print(f"\n✅ {result['message']}")
                    print(f"📝 {product_name} updates list ({language}):")
                    print(result['markdown'])
                    
                    if args.update_files:
                        if create_or_update_index_file(product_name, result['markdown'], language):
                            if language == "en":
                                print(f"✅ Updated {product_name}/updates/index.md")
                            else:
                                print(f"✅ Updated {product_name}/updates/index.{language}.md")
                        else:
                            if language == "en":
                                print(f"❌ Failed to update {product_name}/updates/index.md")
                            else:
                                print(f"❌ Failed to update {product_name}/updates/index.{language}.md")
    
    elif args.language:
        # Generate for specific language
        language = args.language
        if language not in supported_languages:
            print(f"❌ Language '{language}' not supported. Supported languages: {', '.join(supported_languages)}")
            return
        
        if args.product:
            # Generate for specific product and language
            markdown_list, message = generate_updates_list_for_product_and_language(args.product, language)
            print(f"✅ {message}")
            if markdown_list:
                print(f"\nGenerated markdown list for {language}:")
                print(markdown_list)
            
            if args.update_files:
                if create_or_update_index_file(args.product, markdown_list, language):
                    if language == "en":
                        print(f"✅ Updated {args.product}/updates/index.md")
                    else:
                        print(f"✅ Updated {args.product}/updates/index.{language}.md")
                else:
                    if language == "en":
                        print(f"❌ Failed to update {args.product}/updates/index.md")
                    else:
                        print(f"❌ Failed to update {args.product}/updates/index.{language}.md")
        else:
            # Generate for all products and language
            results = generate_all_products_updates_list_for_language(language)
            
            if not results:
                print(f"No products with updates found for {language}.")
                return
            
            print(f"Generated updates lists for all products in {language}:")
            for product_name, result in results.items():
                print(f"\n✅ {result['message']}")
                print(f"📝 {product_name} updates list ({language}):")
                print(result['markdown'])
                
                if args.update_files:
                    if create_or_update_index_file(product_name, result['markdown'], language):
                        if language == "en":
                            print(f"✅ Updated {product_name}/updates/index.md")
                        else:
                            print(f"✅ Updated {product_name}/updates/index.{language}.md")
                    else:
                        if language == "en":
                            print(f"❌ Failed to update {product_name}/updates/index.md")
                        else:
                            print(f"❌ Failed to update {product_name}/updates/index.{language}.md")
    
    else:
        # Original behavior - generate for English only
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
    main()
