#!/usr/bin/env python3
"""
Generate LLM prompt .txt files for English pages missing translations.

For each English base .md file that has at least one missing language variant,
create a concise text file under an output folder containing:
  - Coverage matrix (group + 1/0 per language)
  - Concise translation guidelines (global + language-specific)
  - Brief instructions for LLM translation
  - Source file path reference (no embedded content)

Default output dir: i18n-tools/prompts/
Languages precedence: --languages > --config YAML > mkdocs.yml > defaults.

Usage:
  python3 i18n-tools/i18n_4_generate_prompts.py --docs docs --config i18n-tools/i18n.yml
  python3 i18n-tools/i18n_4_generate_prompts.py --docs docs --output-dir i18n-tools/prompts --overwrite

Notes:
  - Only .md pages are considered
  - Output files use .txt extension with filename suffix .llm-task.txt
  - Translation guides are automatically loaded from i18n-tools/translation_guide/
  - Global guide (global.md) is loaded first, then language-specific guides
  - Prompts are optimized for token efficiency
"""

from __future__ import annotations

import argparse
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


def load_translation_guide(guide_path: str) -> Optional[str]:
    """Load a translation guide from a markdown file."""
    try:
        with open(guide_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


def load_translation_guides(translation_guide_dir: str, languages: List[str]) -> Dict[str, str]:
    """Load translation guides for all languages.
    
    Returns a dictionary mapping language codes to guide content.
    Always loads global guide first, then language-specific guides.
    """
    guides: Dict[str, str] = {}
    
    # Load global guide first
    global_guide_path = os.path.join(translation_guide_dir, "global.md")
    global_guide = load_translation_guide(global_guide_path)
    if global_guide:
        guides["global"] = global_guide
    
    # Load language-specific guides
    for lang in languages:
        if lang == "en":  # Skip English as it's the source
            continue
        lang_guide_path = os.path.join(translation_guide_dir, f"{lang}.md")
        lang_guide = load_translation_guide(lang_guide_path)
        if lang_guide:
            guides[lang] = lang_guide
    
    return guides


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
    parser = argparse.ArgumentParser(description="Generate concise LLM prompt files for missing translations")
    parser.add_argument("--docs", default="docs", help="Docs root directory to scan")
    parser.add_argument("--mkdocs", default="mkdocs.yml", help="Path to mkdocs.yml")
    parser.add_argument("--config", default=None, help="Path to i18n config YAML (default: i18n-tools/i18n.yml if present)")
    parser.add_argument("--languages", default=None, help="Comma-separated expected languages")
    parser.add_argument("--output-dir", default=os.path.join("i18n-tools", "prompts"), help="Directory to write prompt .txt files")
    parser.add_argument("--translation-guide-dir", default=os.path.join("i18n-tools", "translation_guide"), help="Directory containing translation guides")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing prompt files")
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


def read_file_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_text(path: str, content: str, overwrite: bool) -> None:
    if os.path.exists(path) and not overwrite:
        return
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build_prompt_markdown(
    group: str,
    languages: List[str],
    present_langs: Set[str],
    translation_guides: Dict[str, str],
    prompt_file_path: str,
) -> str:
    flags = ["1" if lang in present_langs else "0" for lang in languages]
    csv_line = f"{group}," + ",".join(flags)
    missing = [l for l in languages[1:] if l not in present_langs]
    base_no_ext, ext = os.path.splitext(group)
    targets = [f"docs/{base_no_ext}.{l}{ext}" for l in missing]

    lines: List[str] = []
    lines.append(f"# Translate '{group}' to missing languages")
    lines.append("")
    lines.append(f"**File:** {prompt_file_path}")
    lines.append("")
    lines.append("**Coverage:** " + csv_line)
    lines.append("")
    lines.append("**Targets:**")
    for t in targets:
        lines.append(f"- {t}")
    lines.append("")
    
    # Reference translation guides instead of embedding them
    lines.append("## Translation Guidelines")
    lines.append("")
    lines.append("**IMPORTANT**: Follow the translation guidelines in the `i18n-tools/translation_guide/` directory:")
    lines.append("")
    lines.append("- `global.md` - Universal translation standards")
    
    # List available language-specific guides for missing languages
    available_guides = []
    for lang in missing:
        if lang in translation_guides:
            available_guides.append(f"- `{lang}.md` - {lang.upper()} specific guidelines")
    
    if available_guides:
        lines.append("")
        lines.append("Language-specific guides:")
        lines.extend(available_guides)
    
    lines.append("")
    lines.append("## Instructions")
    lines.append("- Translate English source to each target language")
    lines.append("- Follow guidelines in `i18n-tools/translation_guide/` directory")
    lines.append("- Keep markdown structure, links, images, emojis")
    lines.append("- Don't translate code blocks, URLs, product names")
    lines.append("- Preserve relative links and image paths")
    lines.append("- Use UTF-8, output plain markdown")
    lines.append("")
    lines.append(f"**Source:** docs/{group}")
    lines.append("")
    lines.append("**After completion:** Delete this file")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    languages = determine_languages(args)
    docs_root = os.path.abspath(args.docs)
    out_dir = os.path.abspath(args.output_dir)
    translation_guide_dir = os.path.abspath(args.translation_guide_dir)

    # Load translation guides
    print(f"Loading translation guides from {translation_guide_dir}...")
    translation_guides = load_translation_guides(translation_guide_dir, languages)
    
    if translation_guides:
        print(f"Loaded guides for: {', '.join(translation_guides.keys())}")
    else:
        print("No translation guides found. Proceeding with basic instructions only.")

    groups, group_to_langs = audit_docs(docs_root, languages)

    # For each group, if English present and any non-English missing, emit a prompt file
    total_written = 0
    for group in groups:
        present = group_to_langs.get(group, set())
        if languages[0] not in present:
            continue
        missing_any = any(l not in present for l in languages[1:])
        if not missing_any:
            continue
        # Flatten path into a single filename by replacing '/' with '_'
        base_no_ext, _ext = os.path.splitext(group)
        flattened = base_no_ext.replace("/", "_")
        prompt_name = f"{flattened}.llm-task.txt"
        prompt_abs = os.path.join(out_dir, prompt_name)
        prompt_file_path = os.path.relpath(prompt_abs, os.getcwd())
        prompt_md = build_prompt_markdown(group, languages, present, translation_guides, prompt_file_path)

        write_text(prompt_abs, prompt_md, overwrite=args.overwrite)
        total_written += 1
        print(f"Wrote prompt: {os.path.relpath(prompt_abs, os.getcwd())}")

    print(f"Completed. Wrote {total_written} prompt file(s) to {out_dir}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())