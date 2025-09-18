#!/usr/bin/env python3
"""
Script to manage multi-language configuration in mkdocs.yml
Adds or removes language configurations from the i18n plugin
"""

import os
import sys
import yaml
import argparse
from pathlib import Path


def load_yaml_file(file_path):
    """Load YAML file and return its contents"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Use safe_load for lang.yml, but need to handle custom tags for mkdocs.yml
            if file_path.endswith('lang.yml'):
                return yaml.safe_load(f)
            else:
                # For mkdocs.yml, we need to handle custom tags
                content = f.read()
                # Replace problematic custom tags with safe alternatives
                content = content.replace('!!python/name:material.extensions.emoji.twemoji', 'twemoji')
                content = content.replace('!!python/name:material.extensions.emoji.to_svg', 'to_svg')
                return yaml.safe_load(content)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def save_yaml_file(file_path, data):
    """Save data to YAML file"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        # Restore custom tags if this is mkdocs.yml
        if file_path.endswith('mkdocs.yml'):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Restore the custom tags
            content = content.replace('twemoji', '!!python/name:material.extensions.emoji.twemoji')
            content = content.replace('to_svg', '!!python/name:material.extensions.emoji.to_svg')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return True
    except Exception as e:
        print(f"Error saving {file_path}: {e}")
        return False


def find_i18n_plugin_index(mkdocs_config):
    """Find the index of the i18n plugin in the plugins list"""
    if 'plugins' not in mkdocs_config:
        return -1
    
    for i, plugin in enumerate(mkdocs_config['plugins']):
        if isinstance(plugin, dict) and 'i18n' in plugin:
            return i
    return -1


def add_languages_to_mkdocs(mkdocs_path, lang_path, languages=None):
    """
    Add language configurations to mkdocs.yml from lang.yml
    
    Args:
        mkdocs_path: Path to mkdocs.yml
        lang_path: Path to lang.yml
        languages: List of specific languages to add (None = all)
    """
    # Load configurations
    mkdocs_config = load_yaml_file(mkdocs_path)
    lang_config = load_yaml_file(lang_path)
    
    if not mkdocs_config or not lang_config:
        return False
    
    # Find i18n plugin
    i18n_index = find_i18n_plugin_index(mkdocs_config)
    if i18n_index == -1:
        print("Error: i18n plugin not found in mkdocs.yml")
        return False
    
    # Get current languages
    current_languages = mkdocs_config['plugins'][i18n_index]['i18n'].get('languages', [])
    
    # Filter languages if specific ones requested
    if languages:
        lang_config = [lang for lang in lang_config if lang['locale'] in languages]
    
    # Add languages from lang.yml
    added_count = 0
    for lang_entry in lang_config:
        locale = lang_entry['locale']
        
        # Check if language already exists
        if not any(lang.get('locale') == locale for lang in current_languages):
            # Convert lang.yml format to mkdocs.yml format
            mkdocs_lang_entry = {
                'locale': locale,
                'name': lang_entry['name'],
                'build': lang_entry.get('build', True)
            }
            
            # Add nav_translations if present
            if 'nav_translations' in lang_entry:
                mkdocs_lang_entry['nav_translations'] = lang_entry['nav_translations']
            
            current_languages.append(mkdocs_lang_entry)
            added_count += 1
            print(f"Added language: {locale} ({lang_entry['name']})")
    
    # Update mkdocs config
    mkdocs_config['plugins'][i18n_index]['i18n']['languages'] = current_languages
    
    # Save updated config
    if save_yaml_file(mkdocs_path, mkdocs_config):
        print(f"Successfully added {added_count} languages to mkdocs.yml")
        return True
    else:
        print("Failed to save mkdocs.yml")
        return False


def remove_languages_from_mkdocs(mkdocs_path, languages=None):
    """
    Remove language configurations from mkdocs.yml
    
    Args:
        mkdocs_path: Path to mkdocs.yml
        languages: List of specific languages to remove (None = all except English)
    """
    # Load configuration
    mkdocs_config = load_yaml_file(mkdocs_path)
    
    if not mkdocs_config:
        return False
    
    # Find i18n plugin
    i18n_index = find_i18n_plugin_index(mkdocs_config)
    if i18n_index == -1:
        print("Error: i18n plugin not found in mkdocs.yml")
        return False
    
    # Get current languages
    current_languages = mkdocs_config['plugins'][i18n_index]['i18n'].get('languages', [])
    
    # Determine which languages to remove
    if languages is None:
        # Remove all except English
        languages_to_remove = [lang for lang in current_languages if lang.get('locale') != 'en']
    else:
        # Remove specific languages
        languages_to_remove = [lang for lang in current_languages if lang.get('locale') in languages]
    
    # Remove languages
    removed_count = 0
    for lang in languages_to_remove:
        locale = lang.get('locale')
        if locale != 'en':  # Never remove English
            current_languages.remove(lang)
            removed_count += 1
            print(f"Removed language: {locale} ({lang.get('name', 'Unknown')})")
    
    # Update mkdocs config
    mkdocs_config['plugins'][i18n_index]['i18n']['languages'] = current_languages
    
    # Save updated config
    if save_yaml_file(mkdocs_path, mkdocs_config):
        print(f"Successfully removed {removed_count} languages from mkdocs.yml")
        return True
    else:
        print("Failed to save mkdocs.yml")
        return False


def list_current_languages(mkdocs_path):
    """List currently configured languages in mkdocs.yml"""
    mkdocs_config = load_yaml_file(mkdocs_path)
    
    if not mkdocs_config:
        return False
    
    # Find i18n plugin
    i18n_index = find_i18n_plugin_index(mkdocs_config)
    if i18n_index == -1:
        print("Error: i18n plugin not found in mkdocs.yml")
        return False
    
    # Get current languages
    current_languages = mkdocs_config['plugins'][i18n_index]['i18n'].get('languages', [])
    
    print("Currently configured languages:")
    for lang in current_languages:
        locale = lang.get('locale', 'Unknown')
        name = lang.get('name', 'Unknown')
        build = lang.get('build', True)
        default = lang.get('default', False)
        status = "DEFAULT" if default else ("BUILD" if build else "NO BUILD")
        print(f"  - {locale}: {name} ({status})")
    
    return True


def main():
    parser = argparse.ArgumentParser(description='Manage multi-language configuration in mkdocs.yml')
    parser.add_argument('action', choices=['add', 'remove', 'list'], 
                       help='Action to perform: add, remove, or list languages')
    parser.add_argument('--languages', nargs='+', 
                       help='Specific languages to add/remove (e.g., zh ja ko)')
    parser.add_argument('--mkdocs-path', default='mkdocs.yml',
                       help='Path to mkdocs.yml file (default: mkdocs.yml)')
    parser.add_argument('--lang-path', default='lang.yml',
                       help='Path to lang.yml file (default: lang.yml)')
    
    args = parser.parse_args()
    
    # Convert to absolute paths
    mkdocs_path = os.path.abspath(args.mkdocs_path)
    lang_path = os.path.abspath(args.lang_path)
    
    # Check if files exist
    if not os.path.exists(mkdocs_path):
        print(f"Error: mkdocs.yml not found at {mkdocs_path}")
        return 1
    
    if args.action == 'add' and not os.path.exists(lang_path):
        print(f"Error: lang.yml not found at {lang_path}")
        return 1
    
    # Perform action
    if args.action == 'add':
        success = add_languages_to_mkdocs(mkdocs_path, lang_path, args.languages)
    elif args.action == 'remove':
        success = remove_languages_from_mkdocs(mkdocs_path, args.languages)
    elif args.action == 'list':
        success = list_current_languages(mkdocs_path)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
