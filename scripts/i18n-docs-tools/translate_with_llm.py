#!/usr/bin/env python3
"""
Translate English markdown files to target languages using LLM APIs.

Supports multiple providers:
- LM Studio (local, default)
- OpenAI (GPT-4, GPT-3.5, etc.)
- Anthropic (Claude)

Usage:
    python translate_with_llm.py <target-md-eng-file.md> [options]

Examples:
    # Translate to all missing languages using LM Studio
    python translate_with_llm.py docs/product/kvm-go/updates/article.md

    # Translate to specific languages using OpenAI
    export OPENAI_API_KEY=sk-...
    python translate_with_llm.py docs/product/kvm-go/updates/article.md --provider openai --langs zh,ja,ko

    # Overwrite existing translations
    python translate_with_llm.py docs/product/kvm-go/updates/article.md --overwrite
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Add parent directories to path for imports
script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
sys.path.insert(0, str(project_root / "scripts" / "i18n-shared"))
sys.path.insert(0, str(script_dir))  # Add script directory for providers import

try:
    from lang_loader import I18nConfig, extract_languages_from_lang_yml, get_default_language
except ImportError:
    print("Error: Could not import lang_loader. Make sure scripts/i18n-shared/lang_loader.py exists.")
    sys.exit(1)

from providers.factory import ProviderFactory, get_provider
from providers.base import TranslationProvider


def try_load_yaml(path: str) -> Optional[dict]:
    """Load YAML file safely."""
    try:
        import yaml
    except ImportError:
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


def get_language_name(lang_code: str, lang_yml_data: List[dict]) -> str:
    """Get language name from lang.yml data."""
    for entry in lang_yml_data:
        if isinstance(entry, dict) and entry.get("locale") == lang_code:
            return entry.get("name", lang_code.upper())
    return lang_code.upper()


def build_group_key(rel_path: str, languages: List[str]) -> Tuple[str, str, str]:
    """Extract group key, language, and extension from file path.
    
    Returns:
        (group_key, language, extension)
    """
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


def find_existing_translations(file_path: str, languages: List[str]) -> Set[str]:
    """Find existing translation files for a given English file.
    
    Args:
        file_path: Path to English markdown file
        languages: List of target languages
    
    Returns:
        Set of language codes that already have translations
    """
    existing = set()
    file_path_obj = Path(file_path)
    base_name = file_path_obj.stem
    # Remove language suffix if present
    for lang in languages:
        if base_name.endswith(f".{lang}"):
            base_name = base_name[: -len(lang) - 1]
            break
    
    parent_dir = file_path_obj.parent
    
    for lang in languages:
        if lang == languages[0]:  # Skip source language
            continue
        lang_file = parent_dir / f"{base_name}.{lang}.md"
        if lang_file.exists():
            existing.add(lang)
    
    return existing


def clean_translated_output(translated: str) -> str:
    """Clean translated output to remove unwanted prompt content.
    
    Removes:
    - <think> tags
    - Translation guideline sections
    - Source content in code blocks
    - Any content before the first '---' (frontmatter start)
    
    Args:
        translated: Raw translated output from LLM
    
    Returns:
        Cleaned translated content
    """
    lines = translated.split('\n')
    cleaned_lines = []
    in_frontmatter = False
    found_frontmatter_start = False
    skip_until_frontmatter = True
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip redacted reasoning tags and similar
        if ('<think>' in line or '</think>' in line or 
            '<think>' in line or '</think>' in line or
            line.strip().startswith('<') and line.strip().endswith('>')):
            i += 1
            continue
        
        # Look for frontmatter start
        if line.strip() == '---' and not found_frontmatter_start:
            found_frontmatter_start = True
            skip_until_frontmatter = False
            in_frontmatter = True
            cleaned_lines.append(line)
            i += 1
            continue
        
        # If we haven't found frontmatter yet, skip lines that look like prompt content
        if skip_until_frontmatter:
            # Skip section headers that look like prompt structure
            if (line.startswith('#') and 
                ('翻訳' in line or 'Translation' in line or 'Guía' in line or 
                 'Guidelines' in line or 'ガイドライン' in line or 'ソース' in line or 
                 'Source' in line or 'Instructions' in line or '指示' in line)):
                # Skip until we find frontmatter or actual content
                i += 1
                continue
            # Skip code blocks that contain source content
            if line.strip().startswith('```markdown') or line.strip().startswith('```'):
                # Skip the entire code block
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    i += 1
                if i < len(lines):
                    i += 1  # Skip closing ```
                continue
        
        # Once we've found frontmatter, include everything
        if found_frontmatter_start:
            cleaned_lines.append(line)
        
        i += 1
    
    result = '\n'.join(cleaned_lines).strip()
    
    # If we didn't find frontmatter, try to extract content after removing prompt sections
    if not found_frontmatter_start:
        # Look for the actual content - it should start with frontmatter or a heading
        for i, line in enumerate(lines):
            if line.strip() == '---' or (line.startswith('#') and 'Demo' in line or 'Video' in line):
                # Found start of actual content
                result = '\n'.join(lines[i:]).strip()
                break
    
    return result


def build_translation_prompt(
    source_content: str,
    target_lang: str,
    lang_name: str,
    translation_guides: Dict[str, str]
) -> str:
    """Build translation prompt with guides and source content.
    
    Args:
        source_content: Source markdown content
        target_lang: Target language code
        lang_name: Target language name
        translation_guides: Dictionary of translation guides
    
    Returns:
        Complete translation prompt
    """
    lines = []
    lines.append(f"You are a professional translator. Translate the following markdown content from English to {lang_name}.")
    lines.append("")
    lines.append("## CRITICAL: Output Format")
    lines.append("")
    lines.append("**Your output MUST start directly with the YAML frontmatter (---) and contain ONLY the translated markdown.**")
    lines.append("")
    lines.append("DO NOT include:")
    lines.append("- Any explanations, comments, or reasoning")
    lines.append("- Translation guidelines in the output")
    lines.append("- The source content or code blocks")
    lines.append("- Any section headers like '## Translation Guidelines' or '## Source Content'")
    lines.append("")
    lines.append("Your output should start with:")
    lines.append("```")
    lines.append("---")
    lines.append("draft: false")
    lines.append("...")
    lines.append("```")
    lines.append("")
    lines.append("## Translation Guidelines")
    lines.append("")
    
    # Add global guide
    if "global" in translation_guides:
        lines.append(translation_guides["global"])
        lines.append("")
    
    # Add language-specific guide
    if target_lang in translation_guides:
        lines.append(f"### {lang_name}-Specific Guidelines")
        lines.append("")
        lines.append(translation_guides[target_lang])
        lines.append("")
    
    lines.append("## Source Content to Translate")
    lines.append("")
    lines.append("```markdown")
    lines.append(source_content)
    lines.append("```")
    lines.append("")
    lines.append("## Final Instructions")
    lines.append("")
    lines.append(f"1. Translate the entire markdown content from English to {lang_name}")
    lines.append("2. Preserve all markdown formatting, links, code blocks, and frontmatter structure")
    lines.append("3. Keep brand names, technical terms, URLs, and file paths in English")
    lines.append("4. Maintain the same YAML frontmatter format (translate values, not keys)")
    lines.append("5. Preserve relative links and image paths exactly")
    lines.append("6. **Output ONLY the translated markdown starting with '---' - nothing else**")
    lines.append("")
    lines.append("Now translate the content above. Your output must start with '---' and contain only the translated markdown.")
    
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Translate English markdown files to target languages using LLM APIs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "file",
        help="Path to English markdown file to translate"
    )
    
    parser.add_argument(
        "--provider",
        default="lmstudio",
        choices=ProviderFactory.get_available_providers(),
        help="API provider to use (default: lmstudio)"
    )
    
    parser.add_argument(
        "--langs",
        default=None,
        help="Comma-separated list of target languages (default: all missing languages)"
    )
    
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing translations (default: skip existing)"
    )
    
    parser.add_argument(
        "--api-url",
        default=None,
        help="Override API endpoint URL"
    )
    
    parser.add_argument(
        "--api-key",
        default=None,
        help="Override API key (prefer environment variables)"
    )
    
    parser.add_argument(
        "--model",
        default=None,
        help="Model name to use (provider-specific defaults)"
    )
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.3,
        help="Temperature for generation (default: 0.3)"
    )
    
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Maximum tokens in response (default: auto)"
    )
    
    parser.add_argument(
        "--config-file",
        default=None,
        help="Load configuration from YAML file"
    )
    
    parser.add_argument(
        "--config",
        default=None,
        help="Path to lang.yml (default: docs/assets/i18n-sites/lang.yml)"
    )
    
    parser.add_argument(
        "--mkdocs",
        default="mkdocs.yml",
        help="Path to mkdocs.yml"
    )
    
    parser.add_argument(
        "--translation-guide-dir",
        default=None,
        help="Directory containing translation guides (default: scripts/i18n-docs-tools/translation_guide)"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be translated without making API calls"
    )
    
    return parser.parse_args()


def load_config_file(config_path: str) -> Dict:
    """Load configuration from YAML file."""
    config = try_load_yaml(config_path)
    if not config:
        return {}
    
    # Support environment variable references like ${VAR_NAME}
    def resolve_env_refs(value):
        if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            var_name = value[2:-1]
            return os.getenv(var_name, value)
        return value
    
    def process_dict(d):
        if isinstance(d, dict):
            return {k: resolve_env_refs(process_dict(v)) for k, v in d.items()}
        elif isinstance(d, list):
            return [process_dict(item) for item in d]
        else:
            return resolve_env_refs(d)
    
    return process_dict(config)


def main() -> int:
    """Main entry point."""
    start_time = time.time()
    args = parse_args()
    
    # Resolve paths
    file_path = Path(args.file)
    if not file_path.is_absolute():
        file_path = Path.cwd() / file_path
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return 1
    
    # Load language configuration
    if args.config:
        lang_yml_path = Path(args.config)
    else:
        lang_yml_path = project_root / "docs" / "assets" / "i18n-sites" / "lang.yml"
    
    mkdocs_path = project_root / args.mkdocs
    
    try:
        i18n_config = I18nConfig(lang_yml_path, mkdocs_path)
        languages = i18n_config.languages
        default_lang = i18n_config.default_language
    except Exception as e:
        print(f"Error loading language configuration: {e}")
        return 1
    
    # Load lang.yml data for language names
    lang_yml_data = try_load_yaml(str(lang_yml_path)) or []
    
    # Determine target languages
    if args.langs:
        target_langs = [l.strip() for l in args.langs.split(",") if l.strip()]
        # Validate languages
        invalid = [l for l in target_langs if l not in languages]
        if invalid:
            print(f"Error: Invalid languages: {', '.join(invalid)}")
            print(f"Available languages: {', '.join(languages)}")
            return 1
    else:
        # Find missing translations
        existing = find_existing_translations(str(file_path), languages)
        target_langs = [l for l in languages if l != default_lang and (args.overwrite or l not in existing)]
    
    if not target_langs:
        print("No languages to translate. All translations exist or no target languages specified.")
        return 0
    
    # Load translation guides
    if args.translation_guide_dir:
        guide_dir = Path(args.translation_guide_dir)
    else:
        guide_dir = script_dir / "translation_guide"
    
    translation_guides = load_translation_guides(str(guide_dir), languages)
    
    # Load configuration
    config = {}
    if args.config_file:
        file_config = load_config_file(args.config_file)
        config.update(file_config)
    
    # Override with CLI args
    provider_config = {
        "api_url": args.api_url or config.get("api_url"),
        "api_key": args.api_key or config.get("api_key"),
        "model": args.model or config.get("model"),
        "temperature": args.temperature,
        "max_tokens": args.max_tokens or config.get("max_tokens"),
    }
    
    # Remove None values
    provider_config = {k: v for k, v in provider_config.items() if v is not None}
    
    # Create provider
    try:
        provider = get_provider(args.provider, provider_config)
    except Exception as e:
        print(f"Error creating provider '{args.provider}': {e}")
        print(f"\nAvailable providers: {', '.join(ProviderFactory.get_available_providers())}")
        return 1
    
    # Display provider information
    print("=" * 60)
    print("Translation Configuration")
    print("=" * 60)
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    print(f"Provider: {args.provider}")
    
    # Show provider-specific details
    if hasattr(provider, 'api_url'):
        print(f"API URL: {provider.api_url}")
    if hasattr(provider, 'api_key') and provider.api_key:
        masked_key = provider.api_key[:8] + "..." + provider.api_key[-4:] if len(provider.api_key) > 12 else "***"
        print(f"API Key: {masked_key}")
    
    model = provider.get_model(args.model)
    print(f"Model: {model}")
    print(f"Temperature: {args.temperature}")
    if args.max_tokens:
        print(f"Max Tokens: {args.max_tokens}")
    print("=" * 60)
    print()
    
    # Validate provider configuration
    if not args.dry_run:
        print("🔍 Validating provider connection...")
        try:
            provider.validate_config()
            print("✅ Provider connection validated successfully")
        except Exception as e:
            print(f"❌ Error validating provider configuration: {e}")
            return 1
        print()
    
    # Read source file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source_content = f.read()
    except Exception as e:
        print(f"Error reading source file: {e}")
        return 1
    
    # Determine output file base name
    rel_path = os.path.relpath(file_path, project_root / "docs")
    group_key, source_lang, ext = build_group_key(rel_path, languages)
    
    # Extract base filename without extension and directory
    group_dir = os.path.dirname(group_key)
    group_basename = os.path.basename(group_key)
    base_name = os.path.splitext(group_basename)[0]
    
    # Build output directory
    output_dir = project_root / "docs" / group_dir if group_dir else project_root / "docs"
    
    print("=" * 60)
    print("Translation Task")
    print("=" * 60)
    print(f"Source file: {file_path}")
    print(f"Source language: {source_lang} ({get_language_name(source_lang, lang_yml_data)})")
    print(f"Target languages: {', '.join(target_langs)} ({', '.join([get_language_name(l, lang_yml_data) for l in target_langs])})")
    print(f"Output directory: {output_dir}")
    print("=" * 60)
    print()
    if args.dry_run:
        print("\n" + "=" * 60)
        print("[DRY RUN MODE] - No translations will be performed")
        print("=" * 60)
        print(f"Would translate to {len(target_langs)} language(s):")
        print()
        for lang in target_langs:
            lang_name = get_language_name(lang, lang_yml_data)
            output_file = output_dir / f"{base_name}.{lang}.md"
            exists = "✓ exists" if output_file.exists() else "✗ missing"
            print(f"  • {lang} ({lang_name})")
            print(f"    Output: {output_file}")
            print(f"    Status: {exists}")
            if args.overwrite and output_file.exists():
                print(f"    Note: Will overwrite existing file (--overwrite enabled)")
            print()
        print("=" * 60)
        return 0
    
    print()
    
    # Translate to each target language
    success_count = 0
    error_count = 0
    
    for lang in target_langs:
        lang_name = get_language_name(lang, lang_yml_data)
        output_file = output_dir / f"{base_name}.{lang}.md"
        
        # Check if file exists and overwrite flag
        if output_file.exists() and not args.overwrite:
            print(f"⏭️  Skipping {lang} ({lang_name}): {output_file.name} already exists (use --overwrite to replace)")
            continue
        
        lang_start_time = time.time()
        print(f"🔄 Translating to {lang} ({lang_name})...")
        print(f"   API: {args.provider} @ {getattr(provider, 'api_url', 'N/A')}")
        print(f"   Model: {provider.get_model(args.model)}")
        print(f"   Output: {output_file}")
        
        try:
            # Build prompt
            print(f"   📝 Building translation prompt...")
            prompt = build_translation_prompt(source_content, lang, lang_name, translation_guides)
            prompt_size = len(prompt)
            print(f"   📊 Prompt size: {prompt_size:,} characters")
            
            # Translate
            print(f"   🌐 Calling {args.provider} API...")
            api_start_time = time.time()
            translated = provider.translate(
                prompt,
                model=args.model,
                temperature=args.temperature,
                max_tokens=args.max_tokens
            )
            api_time = time.time() - api_start_time
            translated_size = len(translated)
            print(f"   📥 Received response: {translated_size:,} characters ({api_time:.2f}s)")
            
            # Clean the output to remove any unwanted prompt content
            print(f"   🧹 Cleaning output...")
            cleaned_translated = clean_translated_output(translated)
            cleaned_size = len(cleaned_translated)
            print(f"   ✨ Cleaned output: {cleaned_size:,} characters")
            
            # Write output file
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(cleaned_translated)
            
            lang_time = time.time() - lang_start_time
            print(f"   ✅ Successfully saved to: {output_file}")
            print(f"   ⏱️  Language processing time: {lang_time:.2f}s (API: {api_time:.2f}s)")
            print()
            success_count += 1
        
        except Exception as e:
            lang_time = time.time() - lang_start_time
            print(f"   ❌ Error translating to {lang}: {e}")
            print(f"   Provider: {args.provider}, API: {getattr(provider, 'api_url', 'N/A')}")
            print(f"   ⏱️  Time before error: {lang_time:.2f}s")
            print()
            error_count += 1
    
    total_time = time.time() - start_time
    
    print("=" * 60)
    print("Translation Summary")
    print("=" * 60)
    print(f"✅ Successful: {success_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📊 Total: {success_count + error_count}")
    print(f"⏱️  Total processing time: {total_time:.2f}s ({total_time/60:.2f} minutes)")
    if success_count > 0:
        avg_time = total_time / success_count
        print(f"📈 Average time per translation: {avg_time:.2f}s")
    print("=" * 60)
    
    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

