#!/usr/bin/env python3
"""
Clean all other language markdown files for specific English markdown files.

This script takes a path to an English markdown file or a directory containing
markdown files and removes all their language variants (e.g., .zh.md, .ja.md, etc.) 
while keeping the original English files. Optionally, it can also delete the 
English files themselves.

When processing a directory, it recursively scans all subdirectories for
markdown files and processes each one.

Usage examples:
  python i18n-tools/i18n_5_clean_file.py /path/to/file.md
  python i18n-tools/i18n_5_clean_file.py /path/to/directory
  python i18n-tools/i18n_5_clean_file.py /path/to/file.md --include-base
  python i18n-tools/i18n_5_clean_file.py /path/to/directory --yes
  python i18n-tools/i18n_5_clean_file.py /path/to/directory --include-base --yes
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import List, Optional, Tuple


DEFAULT_LANGUAGES = ["en", "zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]


def try_load_yaml(path: str) -> Optional[dict]:
    try:
        import yaml  # type: ignore
    except Exception:
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return None


def load_languages_from_mkdocs(mkdocs_path: str) -> Tuple[Optional[str], Optional[List[str]]]:
    data = try_load_yaml(mkdocs_path)
    if not data:
        return None, None

    plugins = data.get("plugins") or []
    i18n_cfg = None
    for plugin in plugins:
        if isinstance(plugin, dict):
            if "i18n" in plugin:
                i18n_cfg = plugin.get("i18n")
                break
            if "mkdocs-static-i18n" in plugin:
                i18n_cfg = plugin.get("mkdocs-static-i18n")
                break

    if not isinstance(i18n_cfg, dict):
        return None, None

    default_language = i18n_cfg.get("default_language")
    languages_cfg = i18n_cfg.get("languages")

    langs: Optional[List[str]] = None
    if isinstance(languages_cfg, dict):
        langs = list(languages_cfg.keys())
    elif isinstance(languages_cfg, list):
        langs = [str(x) for x in languages_cfg]
    elif isinstance(languages_cfg, str):
        langs = [x.strip() for x in languages_cfg.split(",") if x.strip()]

    return default_language, langs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean all other language markdown files for English markdown files"
    )
    parser.add_argument(
        "path",
        help="Path to an English markdown file or directory containing markdown files (e.g., /path/to/file.md or /path/to/directory)"
    )
    parser.add_argument(
        "--mkdocs",
        default="mkdocs.yml",
        help="Path to mkdocs.yml (to detect languages)"
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to i18n config YAML (default: i18n-tools/i18n.yml if present)"
    )
    parser.add_argument(
        "--languages",
        default=None,
        help="Comma-separated list of expected languages (overrides mkdocs.yml)"
    )
    parser.add_argument(
        "--include-base",
        action="store_true",
        help="Also delete the base English file (default: keep it)"
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip confirmation prompts and delete immediately"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be deleted without actually deleting"
    )
    return parser.parse_args()


def get_default_config_path() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "i18n.yml")


def load_languages_from_config(config_path: Optional[str]) -> Tuple[Optional[str], Optional[List[str]]]:
    path = config_path or get_default_config_path()
    data = try_load_yaml(path)
    if not data:
        return None, None
    default_language = data.get("default_language")
    languages_cfg = data.get("languages")
    langs: Optional[List[str]] = None
    if isinstance(languages_cfg, list):
        langs = [str(x) for x in languages_cfg]
    elif isinstance(languages_cfg, dict):
        langs = list(languages_cfg.keys())
    elif isinstance(languages_cfg, str):
        langs = [x.strip() for x in languages_cfg.split(",") if x.strip()]
    return default_language, langs


def determine_languages(args: argparse.Namespace) -> List[str]:
    # 1) From CLI
    if args.languages:
        langs = [x.strip() for x in args.languages.split(",") if x.strip()]
        if "en" not in langs:
            langs.insert(0, "en")
        return langs

    # 2) From config YAML
    cfg_default, cfg_langs = load_languages_from_config(args.config)
    if cfg_langs:
        if cfg_default and cfg_default in cfg_langs:
            return [cfg_default] + [l for l in cfg_langs if l != cfg_default]
        return (["en"] + [l for l in cfg_langs if l != "en"]) if "en" in cfg_langs else ["en"] + cfg_langs

    # 3) From mkdocs.yml
    default_lang, langs = load_languages_from_mkdocs(args.mkdocs)
    if langs:
        if default_lang and default_lang in langs:
            langs = [default_lang] + [l for l in langs if l != default_lang]
        elif "en" in langs:
            langs = ["en"] + [l for l in langs if l != "en"]
        else:
            langs = ["en"] + langs
        return langs

    # 4) Fallback
    return DEFAULT_LANGUAGES


def find_language_variants(file_path: str, languages: List[str]) -> List[str]:
    """
    Find all language variant files for the given English file.
    Returns a list of absolute paths to variant files that exist.
    """
    if not os.path.exists(file_path):
        return []

    # Get directory and filename parts
    dir_path = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)

    variants = []
    
    # Check each language (skip the first one which is typically 'en' - the base file)
    for lang in languages[1:]:
        variant_filename = f"{name}.{lang}{ext}"
        variant_path = os.path.join(dir_path, variant_filename)
        if os.path.exists(variant_path):
            variants.append(variant_path)

    return variants


def is_base_markdown_file(file_path: str, languages: List[str]) -> bool:
    """
    Check if a file is a base markdown file (not a language variant).
    Returns True if the file is a base markdown file, False otherwise.
    """
    if not file_path.lower().endswith('.md'):
        return False
    
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)
    
    # Check if the filename ends with any language code
    for lang in languages[1:]:  # Skip the first language (usually 'en')
        if name.endswith(f".{lang}"):
            return False
    
    return True


def scan_directory_for_markdown_files(dir_path: str, languages: List[str]) -> List[str]:
    """
    Recursively scan a directory for base markdown files.
    Returns a list of absolute paths to base markdown files.
    """
    base_files = []
    
    for root, dirs, files in os.walk(dir_path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            # Skip hidden files
            if filename.startswith('.'):
                continue
                
            file_path = os.path.join(root, filename)
            if is_base_markdown_file(file_path, languages):
                base_files.append(file_path)
    
    return base_files


def confirm(prompt: str) -> bool:
    ans = input(f"{prompt} [y/N]: ").strip().lower()
    return ans in {"y", "yes"}


def main() -> int:
    args = parse_args()
    
    # Validate input path
    input_path = os.path.abspath(args.path)
    if not os.path.exists(input_path):
        print(f"Error: Path does not exist: {input_path}", file=sys.stderr)
        return 1

    # Determine languages
    languages = determine_languages(args)
    
    # Determine if input is file or directory
    if os.path.isfile(input_path):
        if not input_path.lower().endswith('.md'):
            print(f"Error: File must be a markdown file (.md): {input_path}", file=sys.stderr)
            return 1
        
        # Process single file
        base_files = [input_path]
        print(f"Processing single file: {input_path}")
    else:
        # Process directory
        base_files = scan_directory_for_markdown_files(input_path, languages)
        if not base_files:
            print(f"No base markdown files found in directory: {input_path}")
            return 0
        print(f"Found {len(base_files)} base markdown file(s) in directory: {input_path}")
    
    # Collect all files to delete
    all_files_to_delete = []
    base_files_to_delete = []
    
    for base_file in base_files:
        # Find language variants for this base file
        variants = find_language_variants(base_file, languages)
        all_files_to_delete.extend(variants)
        
        if args.include_base:
            base_files_to_delete.append(base_file)
    
    # Add base files to deletion list if requested
    if args.include_base:
        all_files_to_delete.extend(base_files_to_delete)
    
    if not all_files_to_delete:
        print("No language variant files found to delete.")
        return 0
    
    # Show what will be deleted
    print(f"\nFound {len(all_files_to_delete)} file(s) to delete:")
    for f in all_files_to_delete:
        print(f"  - {f}")
    
    if args.dry_run:
        print("\nDry run: no files will be deleted.")
        return 0
    
    # Confirm deletion
    if not args.yes:
        if args.include_base:
            prompt = f"\nDelete {len(all_files_to_delete)} file(s) including {len(base_files_to_delete)} base English file(s)?"
        else:
            prompt = f"\nDelete {len(all_files_to_delete)} language variant file(s) (keeping base English files)?"
        
        if not confirm(prompt):
            print("Operation cancelled.")
            return 0
    
    # Delete files
    deleted_count = 0
    failed_count = 0
    
    for file_to_delete in all_files_to_delete:
        try:
            os.remove(file_to_delete)
            print(f"Deleted: {file_to_delete}")
            deleted_count += 1
        except Exception as e:
            print(f"Failed to delete {file_to_delete}: {e}", file=sys.stderr)
            failed_count += 1
    
    print(f"\nCompleted. Deleted {deleted_count} file(s).")
    if failed_count > 0:
        print(f"Failed to delete {failed_count} file(s).")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
