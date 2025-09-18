#!/usr/bin/env python3
"""
Generate i18n-tools/i18n.yml from lang.yml language definitions.

Extraction order and logic:
- Read languages from lang.yml (list of language objects with 'locale' and 'name')
- Determine default_language from:
  1) theme.language in mkdocs.yml
  2) fallback 'en'
- Include all languages from lang.yml that have build: true (or no build field)
- Order languages with default first, then others preserving original order

Usage:
  python3 i18n-tools/i18n_1_from_mkdocs.py --lang lang.yml --mkdocs mkdocs.yml --output i18n-tools/i18n.yml --force

"""

from __future__ import annotations

import argparse
import os
import sys
from typing import List, Optional, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate i18n.yml from lang.yml")
    parser.add_argument("--lang", default="lang.yml", help="Path to lang.yml")
    parser.add_argument("--mkdocs", default="mkdocs.yml", help="Path to mkdocs.yml")
    parser.add_argument(
        "--output", default=os.path.join("i18n-tools", "i18n.yml"), help="Output YAML path"
    )
    parser.add_argument(
        "--force", action="store_true", help="Overwrite output file if it already exists"
    )
    return parser.parse_args()


def try_load_yaml(path: str) -> Optional[dict]:
    try:
        import yaml  # type: ignore
    except Exception:
        print("PyYAML is required. Install with: python3 -m pip install pyyaml", file=sys.stderr)
        return None
    try:
        # Create a permissive loader that treats unknown python/name tags as plain strings
        class PermissiveLoader(yaml.SafeLoader):
            pass

        def construct_python_name(loader, suffix, node):
            # Return the referenced name as a simple string
            return suffix

        yaml.add_multi_constructor(
            "tag:yaml.org,2002:python/name:", construct_python_name, Loader=PermissiveLoader
        )

        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=PermissiveLoader) or {}
    except FileNotFoundError:
        print(f"mkdocs.yml not found at: {path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Failed to read YAML: {e}", file=sys.stderr)
        return None


def extract_languages_from_lang_yml(lang_data: List[dict]) -> List[str]:
    """Extract language codes from lang.yml data"""
    languages: List[str] = []
    
    if not isinstance(lang_data, list):
        return languages
    
    for lang_entry in lang_data:
        if isinstance(lang_entry, dict):
            locale = lang_entry.get("locale")
            if not locale:
                continue
            
            # Check if language should be built
            build = lang_entry.get("build")
            if build is False:
                continue
            
            languages.append(str(locale))
    
    return languages


def extract_theme_language(data: dict) -> Optional[str]:
    theme = data.get("theme") or {}
    if isinstance(theme, dict):
        lang = theme.get("language")
        if isinstance(lang, str) and lang.strip():
            return lang.strip()
    return None


def write_i18n_yaml(output_path: str, default_language: str, languages: List[str]) -> None:
    try:
        import yaml  # type: ignore
    except Exception:
        print("PyYAML is required. Install with: python3 -m pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    # ensure default first
    ordered_langs = [default_language] + [l for l in languages if l != default_language]
    data = {
        "default_language": default_language,
        "languages": ordered_langs,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"Wrote i18n config to {os.path.abspath(output_path)}")


def main() -> int:
    args = parse_args()

    if os.path.exists(args.output) and not args.force:
        print(
            f"Output already exists: {args.output}. Use --force to overwrite.",
            file=sys.stderr,
        )
        return 2

    # Load lang.yml
    lang_data = try_load_yaml(args.lang)
    if not lang_data:
        print(f"Failed to load lang.yml from: {args.lang}", file=sys.stderr)
        return 1
    
    # Load mkdocs.yml for theme language
    mkdocs_data = try_load_yaml(args.mkdocs)
    if not mkdocs_data:
        print(f"Failed to load mkdocs.yml from: {args.mkdocs}", file=sys.stderr)
        return 1

    # Extract languages from lang.yml
    languages = extract_languages_from_lang_yml(lang_data)
    if not languages:
        print("No languages found in lang.yml", file=sys.stderr)
        return 1

    # Determine default language
    theme_lang = extract_theme_language(mkdocs_data)
    default_language = theme_lang or "en"
    
    # Ensure default language is in the languages list
    if default_language not in languages:
        languages.insert(0, default_language)

    write_i18n_yaml(args.output, default_language, languages)
    return 0


if __name__ == "__main__":
    sys.exit(main())


