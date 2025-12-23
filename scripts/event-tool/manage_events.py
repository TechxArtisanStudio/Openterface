#!/usr/bin/env python3
"""
Event Management Tool

Automatically generates docs/event/index.*.md files for all supported languages.
Uses docs/assets/i18n-sites/events.json for event definitions and translations.
Supported languages are loaded from docs/assets/i18n-sites/lang.yml via I18nConfig.

Usage:
    python scripts/event-tool/manage_events.py
    python scripts/event-tool/manage_events.py --language zh
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Add i18n-shared to path for importing I18nConfig
script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
shared_dir = project_root / "scripts" / "i18n-shared"
sys.path.insert(0, str(shared_dir))

from lang_loader import I18nConfig


def load_events_config() -> Dict:
    """Load events.json configuration file."""
    events_path = project_root / "docs" / "assets" / "i18n-sites" / "events.json"
    
    if not events_path.exists():
        raise FileNotFoundError(
            f"events.json not found: {events_path}\n"
            "Please ensure events.json exists in docs/assets/i18n-sites/"
        )
    
    try:
        with open(events_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in events.json: {e}")
    except Exception as e:
        raise RuntimeError(f"Error loading events.json: {e}")


def validate_event_translations(events_config: Dict, i18n_config: I18nConfig) -> None:
    """Validate that events.json has translations for all languages in lang.yml."""
    events = events_config.get("events", [])
    required_languages = set(i18n_config.languages)
    
    for event in events:
        event_id = event.get("id", "unknown")
        translations = event.get("translations", {})
        event_languages = set(translations.keys())
        
        missing = required_languages - event_languages
        if missing:
            print(f"⚠️  Warning: Event '{event_id}' missing translations for: {', '.join(sorted(missing))}")
            print(f"   Will fallback to English for missing languages")
        
        extra = event_languages - required_languages
        if extra:
            print(f"ℹ️  Info: Event '{event_id}' has extra languages not in lang.yml: {', '.join(sorted(extra))}")


def validate_event_folders(events_config: Dict) -> List[Dict]:
    """Validate that event folders exist and return valid events."""
    events = events_config.get("events", [])
    valid_events = []
    event_dir = project_root / "docs" / "event"
    
    for event in events:
        folder = event.get("folder")
        event_id = event.get("id", "unknown")
        
        if not folder:
            print(f"⚠️  Warning: Event '{event_id}' missing 'folder' field, skipping")
            continue
        
        event_path = event_dir / folder
        if not event_path.exists():
            print(f"⚠️  Warning: Event folder not found: {event_path}, skipping event '{event_id}'")
            continue
        
        # Check if updates directory exists
        updates_path = event_path / "updates"
        if not updates_path.exists():
            print(f"⚠️  Warning: Updates directory not found for event '{event_id}': {updates_path}")
            # Still include the event, but the link might not work
        
        valid_events.append(event)
    
    return valid_events


def get_event_translation(event: Dict, language: str, default_language: str = "en") -> str:
    """Get translation for an event in the specified language, fallback to default."""
    translations = event.get("translations", {})
    
    # Try requested language first
    if language in translations:
        return translations[language]
    
    # Fallback to default language
    if default_language in translations:
        return translations[default_language]
    
    # Last resort: use event ID
    return event.get("id", "Unknown Event")


def extract_date_title_and_category(file_path: Path):
    """Extract date and category from frontmatter and H1 title from a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract frontmatter (between --- and ---)
        frontmatter_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        date = None
        category = None
        draft = False
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # Extract date from frontmatter
            date_match = re.search(
                r"^date:\s*(\d{4}-\d{2}-\d{2})", frontmatter, re.MULTILINE
            )
            if date_match:
                date = date_match.group(1)

            # Extract category from frontmatter
            category_match = re.search(
                r'^category:\s*"([^"]*)"', frontmatter, re.MULTILINE
            )
            if category_match:
                category = category_match.group(1)

            # Extract draft status from frontmatter
            draft_match = re.search(
                r"^draft:\s*(true|false)", frontmatter, re.MULTILINE
            )
            if draft_match:
                draft = draft_match.group(1).lower() == "true"

        # Skip if draft is true
        if draft:
            return None, None, None, True

        # Find the first H1 title (line starting with # followed by space)
        lines = content.split("\n")
        title = None
        for line in lines:
            line = line.strip()
            if line.startswith("# "):
                # Remove the # and leading space, return the title
                title = line[2:].strip()
                break

        return date, title, category, False
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None, None, False


def get_update_files_for_event(event_folder: str, language: str, default_language: str = "en") -> List[Dict]:
    """Get information about all update files for an event in a specific language."""
    event_dir = project_root / "docs" / "event" / event_folder
    updates_dir = event_dir / "updates"
    
    if not updates_dir.exists():
        return []
    
    update_files = []
    processed_base_files = set()
    
    # First, collect all base English files
    english_files = {}
    for file_path in updates_dir.glob("*.md"):
        if file_path.name == "index.md" or file_path.name.startswith("index."):
            continue  # Skip index files
        
        # Skip translated files when collecting English files
        if any(
            file_path.name.endswith(f".{lang}.md")
            for lang in ["zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]
        ):
            continue
        
        date, title, category, is_draft = extract_date_title_and_category(file_path)
        if is_draft:
            continue
        if title:
            english_files[file_path.name] = {
                "filename": file_path.name,
                "title": title,
                "raw_date": date,
                "category": category,
            }
    
    if language == default_language:
        # For default language, return all English files
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
                update_files.append({
                    "filename": file_path.name,
                    "title": title,
                    "raw_date": date,
                    "category": category,
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


def get_page_metadata(events_config: Dict, language: str, default_language: str = "en") -> Dict[str, str]:
    """Get page metadata (title, description, keywords) for a language."""
    metadata = events_config.get("page_metadata", {})
    
    if language in metadata:
        return metadata[language]
    
    if default_language in metadata:
        return metadata[default_language]
    
    # Default fallback
    return {
        "title": "Events",
        "description": "Openterface events, exhibitions, and community activities",
        "keywords": "Openterface events, exhibitions, contests, community activities"
    }


def generate_event_index_content(events_config: Dict, language: str, i18n_config: I18nConfig) -> str:
    """Generate markdown content for event index page in specified language."""
    valid_events = validate_event_folders(events_config)
    
    if not valid_events:
        print(f"⚠️  Warning: No valid events found for language {language}")
        return ""
    
    # Get metadata
    metadata = get_page_metadata(events_config, language, i18n_config.default_language)
    
    # Generate frontmatter
    frontmatter = f"""---
title: {metadata['title']}
description: {metadata['description']}
keywords: {metadata['keywords']}
---

# {metadata['title']}

"""
    
    # Generate event sections with individual update pages
    sections = []
    
    for event in valid_events:
        event_name = get_event_translation(event, language, i18n_config.default_language)
        folder = event.get("folder")
        
        sections.append(f"## {event_name}\n")
        
        # Get update files for this event
        update_files = get_update_files_for_event(folder, language, i18n_config.default_language)
        
        if update_files:
            # Sort by date (newest first)
            update_files.sort(key=lambda x: x["raw_date"] or "", reverse=True)
            
            # Generate list of update pages
            for update in update_files:
                date = update["raw_date"] or "Unknown Date"
                title = update["title"]
                filename = update["filename"]
                # Use relative path from event index
                link_path = f"{folder}/updates/{filename}"
                sections.append(f"- {date}: [{title}]({link_path})")
        else:
            # No updates found, show empty section
            pass
        
        sections.append("")  # Empty line after each event section
    
    return frontmatter + "\n".join(sections)


def generate_event_index_file(events_config: Dict, language: str, i18n_config: I18nConfig) -> bool:
    """Generate event index file for a specific language."""
    content = generate_event_index_content(events_config, language, i18n_config)
    
    if not content:
        print(f"⚠️  Warning: No content generated for language {language}")
        return False
    
    # Determine filename
    event_dir = project_root / "docs" / "event"
    if language == i18n_config.default_language:
        index_filename = "index.md"
    else:
        index_filename = f"index.{language}.md"
    
    index_path = event_dir / index_filename
    
    # Ensure directory exists
    event_dir.mkdir(parents=True, exist_ok=True)
    
    # Write file
    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Generated: {index_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to write {index_path}: {e}")
        return False


def generate_all_event_indexes(events_config: Dict, i18n_config: I18nConfig, languages: Optional[List[str]] = None) -> None:
    """Generate event index files for all specified languages (or all languages from lang.yml)."""
    if languages is None:
        languages = i18n_config.languages
    
    print(f"\n{'='*60}")
    print(f"Generating event index files for {len(languages)} language(s)")
    print(f"{'='*60}\n")
    
    success_count = 0
    for language in languages:
        print(f"🌍 Processing language: {language}")
        if generate_event_index_file(events_config, language, i18n_config):
            success_count += 1
        print()
    
    print(f"{'='*60}")
    print(f"✅ Successfully generated {success_count}/{len(languages)} event index files")
    print(f"{'='*60}\n")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Generate event index files for all supported languages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--language",
        help="Generate index for specific language only (default: all languages)"
    )
    
    args = parser.parse_args()
    
    try:
        # Load i18n configuration (single source of truth for languages)
        print("Loading i18n configuration from lang.yml...")
        i18n_config = I18nConfig()
        print(f"✅ Found {len(i18n_config.languages)} supported languages: {', '.join(i18n_config.languages)}")
        
        # Load events configuration
        print("\nLoading events configuration from events.json...")
        events_config = load_events_config()
        events_count = len(events_config.get("events", []))
        print(f"✅ Loaded {events_count} event(s)")
        
        # Validate translations
        print("\nValidating event translations...")
        validate_event_translations(events_config, i18n_config)
        
        # Determine which languages to process
        if args.language:
            if args.language not in i18n_config.languages:
                print(f"❌ Error: Language '{args.language}' not found in lang.yml")
                print(f"   Supported languages: {', '.join(i18n_config.languages)}")
                sys.exit(1)
            languages_to_process = [args.language]
        else:
            languages_to_process = i18n_config.languages
        
        # Generate index files
        generate_all_event_indexes(events_config, i18n_config, languages_to_process)
        
        print("✅ Event index generation completed successfully!")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

