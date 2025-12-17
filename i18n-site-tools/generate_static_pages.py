#!/usr/bin/env python3
"""
Static Page Generator for i18n

This script generates static HTML files from templates with data-i18n-key attributes
and translation JSON files. This provides SEO-friendly static content for each language.

Usage:
    python generate_static_pages.py --template home
    python generate_static_pages.py --all
"""

import argparse
import json
import re
import yaml
from pathlib import Path
from typing import Dict
from i18n_config import I18nConfig


class StaticPageGenerator:
    """Generates static HTML pages from templates with i18n translations."""
    
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.templates_dir = self.script_dir / "templates"
        self.i18n_dir = self.script_dir.parent / "docs" / "assets" / "i18n-sites"
        self.output_dir = self.script_dir.parent / "docs" / "overrides"
        self.partials_dir = self.script_dir.parent / "docs" / "partials"
        
        # Load centralized i18n config
        self.i18n_config = I18nConfig()
    
    def generate_hreflang_partial(self) -> None:
        """Generate docs/partials/hreflang.html from i18n.yml."""
        print("\n📝 Generating hreflang partial...")
        self.i18n_config.generate_hreflang_file(self.partials_dir)
    
    def load_i18n_config(self, template_name: str) -> Dict:
        """Load i18n configuration for a template."""
        i18n_path = self.i18n_dir / f"{template_name}.json"
        
        if not i18n_path.exists():
            raise FileNotFoundError(
                f"i18n configuration file not found: {i18n_path}\n"
                f"Please ensure {template_name}.json exists in {self.i18n_dir}"
            )
        
        try:
            with open(i18n_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {template_name}.json: {e}")
        except Exception as e:
            raise RuntimeError(f"Error loading {template_name}.json: {e}")
    
    def generate_page(self, template_name: str, language: str, translations: Dict) -> str:
        """Generate a static page for a specific language using regex (preserves Jinja2)."""
        # Load template
        template_path = self.templates_dir / f"{template_name}-base.html"
        
        if not template_path.exists():
            raise FileNotFoundError(
                f"Template not found: {template_path}\n"
                f"Please ensure {template_name}-base.html exists in {self.templates_dir}"
            )
        
        # Read template as text (preserves Jinja2 syntax)
        with open(template_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Step 1: Replace content attribute in meta tags with data-i18n-key
        # Pattern: <meta ...content="VALUE"...data-i18n-key="KEY"...>
        def replace_meta_content(match):
            """Replace content attribute value in meta tags."""
            full_tag = match.group(0)
            key = match.group(1)
            
            # Find the content attribute value
            content_match = re.search(r'content=["\']([^"\']*)["\']', full_tag)
            if not content_match:
                return full_tag
            
            original_content = content_match.group(1)
            
            # Get translation for this key (use original content if not found)
            translated_text = translations.get(key, original_content)
            
            # Replace the content attribute value
            result = re.sub(
                r'content=["\'][^"\']*["\']',
                f'content="{translated_text}"',
                full_tag,
                count=1
            )
            
            return result
        
        # Find all meta tags with data-i18n-key and replace their content attribute
        # Pattern: <meta ...data-i18n-key="KEY"...>
        meta_pattern = r'<meta[^>]*data-i18n-key=["\']([^"\']+)["\'][^>]*>'
        html_content = re.sub(meta_pattern, replace_meta_content, html_content, flags=re.IGNORECASE)
        
        # Step 2: Replace text content for regular elements with data-i18n-key
        # Pattern matches: <tag ...data-i18n-key="key"...>TEXT</tag>
        def replace_i18n_text(match):
            """Replace text content with translation."""
            tag_name = match.group(1)
            attributes_and_key = match.group(2)
            key = match.group(3)
            content = match.group(4)
            
            # Get translation for this key (use original content if not found)
            translated_text = translations.get(key, content)
            
            # Return the tag with translated text (attributes unchanged for now)
            return f'<{tag_name}{attributes_and_key}>{translated_text}</{tag_name}>'
        
        # Find all non-meta elements with data-i18n-key and replace their text
        # Pattern: <tag (attributes including data-i18n-key="KEY")>CONTENT</tag>
        pattern = r'<(\w+)([^>]*data-i18n-key=["\']([^"\']+)["\'][^>]*)>(.*?)</\1>'
        html_content = re.sub(pattern, replace_i18n_text, html_content, flags=re.DOTALL)
        
        # Step 3: Remove ALL data-i18n-key attributes from the HTML
        html_content = re.sub(r'\s*data-i18n-key=["\'][^"\']*["\']', '', html_content)
        
        # Step 4: Remove ALL data-i18n-file attributes
        html_content = re.sub(r'\s*data-i18n-file=["\'][^"\']*["\']', '', html_content)
        
        return html_content
    
    def generate_template(self, template_name: str, language: str = None):
        """Generate static pages for a template."""
        print(f"\n{'='*60}")
        print(f"Generating static pages for: {template_name}")
        print(f"{'='*60}\n")
        
        # Load i18n configuration
        i18n_config = self.load_i18n_config(template_name)
        json_languages = i18n_config.get('supported_languages', [])
        all_translations = i18n_config.get('translations', {})
        
        # Validate JSON languages against YAML config
        self.i18n_config.validate_json_languages(json_languages, f"{template_name}.json")
        
        # Use intersection of YAML and JSON languages
        yaml_languages = set(self.i18n_config.languages)
        supported_languages = list(set(json_languages) & yaml_languages)
        
        if not supported_languages:
            raise ValueError(
                f"No common languages between i18n.yml and {template_name}.json"
            )
        
        # Sort to ensure consistent order
        supported_languages.sort()
        
        # Determine which languages to generate
        if language:
            if language not in supported_languages:
                raise ValueError(
                    f"Language '{language}' not supported for {template_name}. "
                    f"Supported: {', '.join(supported_languages)}"
                )
            languages_to_generate = [language]
        else:
            languages_to_generate = supported_languages
        
        print(f"📊 Generating for {len(languages_to_generate)} language(s): {', '.join(languages_to_generate)}\n")
        
        # Generate page for each language
        for lang in languages_to_generate:
            translations = all_translations.get(lang, {})
            
            if not translations:
                print(f"⚠️  Warning: No translations found for '{lang}', skipping...")
                continue
            
            # Generate the page
            html_content = self.generate_page(template_name, lang, translations)
            
            # Determine output filename
            suffix = '' if lang == 'en' else f'.{lang}'
            output_filename = f"{template_name}{suffix}.html"
            output_path = self.output_dir / output_filename
            
            # Write output
            output_path.write_text(html_content, encoding='utf-8')
            print(f"  ✅ Generated: {output_filename} ({lang})")
        
        print(f"\n✅ Generation complete!")
        print(f"📄 Output directory: {self.output_dir}\n")
    
    def generate_all(self):
        """Generate all available templates."""
        print("\n" + "="*60)
        print("Generating ALL static pages")
        print("="*60)
        
        # Generate hreflang partial first (used by all templates)
        self.generate_hreflang_partial()
        
        # Find all template files
        template_files = list(self.templates_dir.glob("*-base.html"))
        
        if not template_files:
            print(f"\n⚠️  No templates found in {self.templates_dir}")
            print("Template files should be named: <name>-base.html")
            return
        
        print(f"\nFound {len(template_files)} template(s):")
        for template_file in template_files:
            template_name = template_file.stem.replace('-base', '')
            print(f"  - {template_name}")
        
        # Generate each template
        for template_file in template_files:
            template_name = template_file.stem.replace('-base', '')
            try:
                self.generate_template(template_name)
            except Exception as e:
                print(f"\n❌ Error generating {template_name}: {e}\n")
                continue
        
        print("="*60)
        print("All templates generated successfully!")
        print("="*60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate static HTML pages with i18n translations"
    )
    
    parser.add_argument(
        '--template',
        type=str,
        help='Template name to generate (e.g., "home")'
    )
    
    parser.add_argument(
        '--language',
        type=str,
        help='Specific language to generate (e.g., "zh", "ja"). If not specified, generates all languages.'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Generate all available templates'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.template and not args.all:
        parser.error("Either --template or --all must be specified")
    
    if args.template and args.all:
        parser.error("Cannot specify both --template and --all")
    
    # Create generator
    generator = StaticPageGenerator()
    
    try:
        if args.all:
            generator.generate_all()
        else:
            generator.generate_template(args.template, args.language)
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())

