#!/usr/bin/env python3
"""
Audit translation coverage of docs (Markdown only) across languages.

Scans a docs directory recursively for files like:
  - about.md (base language, typically English)
  - about.de.md, about.es.md, about.fr.md, ... (translated variants)

Expected languages are determined in this order:
  1) --languages CLI option (comma-separated)
  2) lang.yml (see --config or docs/assets/i18n-sites/lang.yml)
  3) mkdocs.yml (plugins.i18n or plugins.mkdocs-static-i18n)
  4) Fallback default set: en,zh,ja,ko,fr,de,it,es,pt,ro

Outputs a CSV with columns: group, <lang1>, <lang2>, ... where each cell is 1 (present) or 0 (missing).
Group is the logical base path including extension (e.g., "about.md" or "path/to/page.md").

Usage examples:
  python scripts/i18n-docs-tools/audit_translations.py --docs docs --output i18n_audit.csv
  python scripts/i18n-docs-tools/audit_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml

Exit code is 0 if no rows have missing translations, else 1 when --fail-on-missing is provided.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from typing import Dict, List, Optional, Set, Tuple


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
    """
    Attempts to read default language and languages set from mkdocs.yml.
    Supports either 'i18n' or 'mkdocs-static-i18n' plugin configs.
    Returns (default_language, languages) — where either may be None if not found.
    """
    data = try_load_yaml(mkdocs_path)
    if not data:
        return None, None

    plugins = data.get("plugins") or []
    # Plugins can be a list of strings or a list of dicts
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
    parser = argparse.ArgumentParser(description="Audit i18n coverage for docs")
    parser.add_argument("--docs", default="docs", help="Docs root directory to scan")
    parser.add_argument(
        "--mkdocs", default="mkdocs.yml", help="Path to mkdocs.yml (to detect languages)"
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to lang.yml (default: docs/assets/i18n-sites/lang.yml)",
    )
    parser.add_argument(
        "--languages",
        default=None,
        help="Comma-separated list of expected languages (overrides mkdocs.yml)",
    )
    parser.add_argument(
        "--output",
        default="i18n_audit.csv",
        help="CSV output file path",
    )
    parser.add_argument(
        "--only-missing",
        action="store_true",
        help="Include only rows with at least one missing translation",
    )
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Exit with code 1 if any missing entries are found",
    )
    return parser.parse_args()


def get_default_lang_yml_path() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    return os.path.join(project_root, "docs", "assets", "i18n-sites", "lang.yml")


def load_languages_from_lang_yml(lang_yml_path: Optional[str], mkdocs_path: Optional[str] = None) -> Tuple[Optional[str], Optional[List[str]]]:
    """
    Load languages from lang.yml directly.
    
    Args:
        lang_yml_path: Path to lang.yml (default: docs/assets/i18n-sites/lang.yml)
        mkdocs_path: Path to mkdocs.yml (default: mkdocs.yml in project root)
    
    Returns:
        Tuple of (default_language, languages_list)
    """
    import sys
    from pathlib import Path
    
    # Add shared loader to path
    script_dir = Path(__file__).parent
    shared_dir = script_dir.parent / "i18n-shared"
    if str(shared_dir) not in sys.path:
        sys.path.insert(0, str(shared_dir))
    
    from lang_loader import extract_languages_from_lang_yml, get_default_language
    
    # Resolve paths
    if lang_yml_path is None:
        lang_yml_path = get_default_lang_yml_path()
    
    if mkdocs_path is None:
        script_dir = Path(__file__).parent
        project_root = script_dir.parent.parent
        mkdocs_path = str(project_root / "mkdocs.yml")
    
    # Load lang.yml
    lang_data = try_load_yaml(lang_yml_path)
    if not lang_data or not isinstance(lang_data, list):
        return None, None
    
    # Extract languages
    languages = extract_languages_from_lang_yml(lang_data)
    
    # Get default language
    default_language = get_default_language(Path(mkdocs_path))
    
    return default_language, languages


def determine_languages(args: argparse.Namespace) -> Tuple[str, List[str]]:
    # 1) From CLI
    if args.languages:
        langs = [x.strip() for x in args.languages.split(",") if x.strip()]
        default_lang = langs[0] if langs else "en"
        if "en" not in langs:
            langs.insert(0, "en")
        return default_lang, langs

    # 2) From lang.yml
    cfg_default, cfg_langs = load_languages_from_lang_yml(args.config, args.mkdocs)
    if cfg_langs:
        if cfg_default and cfg_default in cfg_langs:
            ordered = [cfg_default] + [l for l in cfg_langs if l != cfg_default]
            return cfg_default, ordered
        cfg_langs = ["en"] + [l for l in cfg_langs if l != "en"] if "en" in cfg_langs else ["en"] + cfg_langs
        return "en", cfg_langs

    # 3) From mkdocs.yml
    default_lang, langs = load_languages_from_mkdocs(args.mkdocs)
    if langs:
        if default_lang and default_lang in langs:
            ordered = [default_lang] + [l for l in langs if l != default_lang]
            return default_lang, ordered
        # ensure en first
        langs = ["en"] + [l for l in langs if l != "en"] if "en" in langs else ["en"] + langs
        return "en", langs

    # 4) Fallback
    return "en", DEFAULT_LANGUAGES


def iter_docs_files(docs_root: str) -> List[str]:
    result: List[str] = []
    for root, _dirs, files in os.walk(docs_root):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext == ".md":  # Only Markdown files now
                result.append(os.path.join(root, fname))
    return result


def build_group_key(rel_path: str, languages: List[str]) -> Tuple[str, str, str]:
    """
    Returns (group_key, language, ext)
    group_key is the logical base path including extension, e.g., "about.md" or "policy/index.md".
    language is one of the expected languages. Unsuffixed base is treated as default language (usually 'en').
    """
    # Normalize and split
    dir_part, fname = os.path.split(rel_path)
    name, ext = os.path.splitext(fname)
    ext = ext.lower()

    # Prefer longer language codes first (e.g., pt-BR before pt)
    lang_candidates = sorted(languages, key=len, reverse=True)

    lang: Optional[str] = None
    base_name = name
    for l in lang_candidates:
        if name.endswith(f".{l}"):
            lang = l
            base_name = name[: -len(l) - 1]
            break

    if lang is None:
        # Treat unsuffixed as default language (first in languages list)
        lang = languages[0]
        base_name = name

    group_fname = f"{base_name}{ext}"
    group_key = os.path.join(dir_part, group_fname) if dir_part else group_fname
    return group_key.replace(os.sep, "/"), lang, ext


def audit_docs(docs_root: str, languages: List[str]) -> Tuple[List[str], Dict[str, Set[str]]]:
    """
    Returns (groups_sorted, group_to_langs)
    where group_to_langs maps group_key -> set of languages present.
    """
    group_to_langs: Dict[str, Set[str]] = {}
    abs_docs_root = os.path.abspath(docs_root)

    for abs_path in iter_docs_files(abs_docs_root):
        rel_path = os.path.relpath(abs_path, abs_docs_root)
        # Skip hidden files or dirs
        if any(part.startswith(".") for part in rel_path.split(os.sep)):
            continue
        group_key, lang, _ext = build_group_key(rel_path, languages)
        group_to_langs.setdefault(group_key, set()).add(lang)

    groups_sorted = sorted(group_to_langs.keys())
    return groups_sorted, group_to_langs


def write_csv(
    output_path: str,
    groups: List[str],
    group_to_langs: Dict[str, Set[str]],
    languages: List[str],
    only_missing: bool,
) -> int:
    missing_rows = 0
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        header = ["group"] + languages
        writer.writerow(header)
        for group in groups:
            present = group_to_langs.get(group, set())
            row: List[str] = [group]
            any_missing = False
            for lang in languages:
                is_present = lang in present
                if not is_present:
                    any_missing = True
                row.append("1" if is_present else "0")
            if only_missing and not any_missing:
                continue
            if any_missing:
                missing_rows += 1
            writer.writerow(row)
    return missing_rows


def main() -> int:
    args = parse_args()

    default_lang, languages = determine_languages(args)
    # Ensure unique while preserving order
    seen: Set[str] = set()
    ordered_langs: List[str] = []
    for l in languages:
        if l not in seen:
            seen.add(l)
            ordered_langs.append(l)
    languages = ordered_langs

    groups, group_to_langs = audit_docs(args.docs, languages)
    missing_count = write_csv(args.output, groups, group_to_langs, languages, args.only_missing)

    print(
        f"Wrote CSV to {os.path.abspath(args.output)} with {len(groups)} group(s). "
        f"Missing rows: {missing_count}. Default language: {default_lang}."
    )
    if args.fail_on_missing and missing_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())


