#!/usr/bin/env python3
"""
Interactive tool to clean up orphaned translations (no English base file).

- Scans docs/ recursively for .md files only
- Groups language variants: base.md (en), base.de.md, base.es.md, ...
- Lists groups where English (unsuffixed) is missing but at least one other language exists
  in CSV-like lines: group, en, zh, ja, ko, fr, de, it, es, pt, ro (1=present, 0=missing)
- Prompts to delete all translations for those orphaned groups: confirm ALL or per-group
- Language precedence: --languages > i18n config YAML (--config or i18n-tools/i18n.yml) > mkdocs.yml > defaults

Usage examples:
  python i18n-tools/i18n_3_cleanup.py --docs docs
  python i18n-tools/i18n_3_cleanup.py --docs docs --yes-all   # delete all without prompts
  python i18n-tools/i18n_3_cleanup.py --docs docs --dry-run   # list only, no deletions
  python i18n-tools/i18n_3_cleanup.py --docs docs --languages en,zh,ja,ko,fr,de,it,es,pt,ro
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, List, Optional, Set, Tuple
import subprocess


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
    parser = argparse.ArgumentParser(description="Delete translations when English base is missing")
    parser.add_argument("--docs", default="docs", help="Docs root directory to scan")
    parser.add_argument("--mkdocs", default="mkdocs.yml", help="Path to mkdocs.yml")
    parser.add_argument("--config", default=None, help="Path to i18n config YAML (default: i18n-tools/i18n.yml if present)")
    parser.add_argument("--languages", default=None, help="Comma-separated expected languages")
    parser.add_argument("--dry-run", action="store_true", help="List candidates only; do not delete")
    parser.add_argument("--yes-all", action="store_true", help="Delete all candidates without prompting")
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
    if args.languages:
        langs = [x.strip() for x in args.languages.split(",") if x.strip()]
        if "en" not in langs:
            langs.insert(0, "en")
        return langs
    cfg_default, cfg_langs = load_languages_from_config(args.config)
    if cfg_langs:
        if cfg_default and cfg_default in cfg_langs:
            return [cfg_default] + [l for l in cfg_langs if l != cfg_default]
        return (["en"] + [l for l in cfg_langs if l != "en"]) if "en" in cfg_langs else ["en"] + cfg_langs
    default_lang, langs = load_languages_from_mkdocs(args.mkdocs)
    if langs:
        if default_lang and default_lang in langs:
            langs = [default_lang] + [l for l in langs if l != default_lang]
        elif "en" in langs:
            langs = ["en"] + [l for l in langs if l != "en"]
        else:
            langs = ["en"] + langs
        return langs
    return DEFAULT_LANGUAGES


def iter_docs_files(docs_root: str) -> List[str]:
    result: List[str] = []
    for root, _dirs, files in os.walk(docs_root):
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext == ".md":  # Only Markdown files now
                result.append(os.path.join(root, fname))
    return result


def build_group_key(rel_path: str, languages: List[str]) -> Tuple[str, str, str]:
    # Returns (group_key, language, ext)
    dir_part, fname = os.path.split(rel_path)
    name, ext = os.path.splitext(fname)
    ext = ext.lower()

    lang_candidates = sorted(languages, key=len, reverse=True)
    lang: Optional[str] = None
    base_name = name
    for l in lang_candidates:
        if name.endswith(f".{l}"):
            lang = l
            base_name = name[: -len(l) - 1]
            break

    if lang is None:
        lang = languages[0]  # treat unsuffixed as default (usually 'en')
        base_name = name

    group_fname = f"{base_name}{ext}"
    group_key = os.path.join(dir_part, group_fname) if dir_part else group_fname
    return group_key.replace(os.sep, "/"), lang, ext


def audit_docs(docs_root: str, languages: List[str]) -> Tuple[List[str], Dict[str, Set[str]]]:
    group_to_langs: Dict[str, Set[str]] = {}
    abs_docs_root = os.path.abspath(docs_root)
    for abs_path in iter_docs_files(abs_docs_root):
        rel_path = os.path.relpath(abs_path, abs_docs_root)
        if any(part.startswith(".") for part in rel_path.split(os.sep)):
            continue
        group_key, lang, _ext = build_group_key(rel_path, languages)
        group_to_langs.setdefault(group_key, set()).add(lang)
    groups_sorted = sorted(group_to_langs.keys())
    return groups_sorted, group_to_langs


def print_candidates(groups: List[str], group_to_langs: Dict[str, Set[str]], languages: List[str]) -> List[str]:
    candidates: List[str] = []
    for group in groups:
        present = group_to_langs.get(group, set())
        en_present = languages[0] in present  # first language is default (en)
        if en_present:
            continue
        if not any(l in present for l in languages[1:]):
            continue
        row_bits = ["1" if l in present else "0" for l in languages]
        line = f"{group}," + ",".join(row_bits)
        candidates.append(line)
    if candidates:
        print("The following groups have translations but no English base:")
        for line in candidates:
            print(line)
    else:
        print("No orphaned translation groups found.")
    return candidates


def files_for_group(docs_root: str, group: str, languages: List[str]) -> List[str]:
    # Return absolute paths of present files for this group across all languages
    abs_docs_root = os.path.abspath(docs_root)
    base_no_ext, ext = os.path.splitext(group)
    results: List[str] = []
    for idx, lang in enumerate(languages):
        if idx == 0:
            candidate = os.path.join(abs_docs_root, group)
        else:
            candidate = os.path.join(abs_docs_root, f"{base_no_ext}.{lang}{ext}")
        if os.path.exists(candidate):
            results.append(candidate)
    return results


def confirm(prompt: str) -> bool:
    ans = input(f"{prompt} [y/N]: ").strip().lower()
    return ans in {"y", "yes"}


def run_audit(docs_root: str, mkdocs_path: str, config_path: Optional[str]) -> None:
    """Run i18n_2_audit.py to refresh i18n_audit.csv in repo root."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audit_script = os.path.join(script_dir, "i18n_2_audit.py")
    if not os.path.exists(audit_script):
        print("Audit script not found:", audit_script)
        return
    try:
        print("Running audit to refresh i18n_audit.csv ...")
        cmd = [
            sys.executable,
            audit_script,
            "--docs",
            docs_root,
            "--mkdocs",
            mkdocs_path,
            "--output",
            "i18n_audit.csv",
        ]
        cfg_path = config_path or get_default_config_path()
        if os.path.exists(cfg_path):
            cmd.extend(["--config", cfg_path])
        subprocess.run(cmd, check=False)
    except Exception as e:
        print(f"Failed to run audit: {e}")


def main() -> int:
    args = parse_args()
    languages = determine_languages(args)
    docs_root = args.docs

    groups, group_to_langs = audit_docs(docs_root, languages)
    candidates_lines = print_candidates(groups, group_to_langs, languages)

    if not candidates_lines:
        return 0

    # Map lines back to group keys for deletion
    candidate_groups = [line.split(",", 1)[0] for line in candidates_lines]

    if args.dry_run:
        print("Dry run: no files will be deleted.")
        return 0

    if args.yes_all:
        to_delete: List[str] = []
        for group in candidate_groups:
            to_delete.extend(files_for_group(docs_root, group, languages))
        for path in to_delete:
            try:
                os.remove(path)
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
        print(f"Completed. Deleted {len(to_delete)} file(s).")
        if to_delete:
            run_audit(docs_root, args.mkdocs, args.config)
        return 0

    # Ask to delete all at once
    if confirm(f"Delete ALL translations for {len(candidate_groups)} group(s)?"):
        to_delete: List[str] = []
        for group in candidate_groups:
            to_delete.extend(files_for_group(docs_root, group, languages))
        for path in to_delete:
            try:
                os.remove(path)
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
        print(f"Completed. Deleted {len(to_delete)} file(s).")
        if to_delete:
            run_audit(docs_root, args.mkdocs, args.config)
        return 0

    # Otherwise confirm one-by-one
    total_deleted = 0
    for group in candidate_groups:
        if confirm(f"Delete translations for group '{group}'?"):
            paths = files_for_group(docs_root, group, languages)
            for path in paths:
                try:
                    os.remove(path)
                    print(f"Deleted: {path}")
                    total_deleted += 1
                except Exception as e:
                    print(f"Failed to delete {path}: {e}")
    print(f"Completed. Deleted {total_deleted} file(s).")
    if total_deleted:
        run_audit(docs_root, args.mkdocs, args.config)
    return 0


if __name__ == "__main__":
    sys.exit(main())


