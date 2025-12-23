#!/usr/bin/env python3
"""
Script to sync redirect mappings from mkdocs.yml to 404.html
This ensures the 404.html redirect mappings stay in sync with mkdocs.yml
"""

import re
from pathlib import Path

import yaml


def extract_redirects_from_mkdocs():
    """Extract redirect mappings from mkdocs.yml"""
    mkdocs_path = Path(__file__).parent.parent / "mkdocs.yml"

    with open(mkdocs_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the redirects section
    redirects_match = re.search(
        r"- redirects:\s*\n\s*redirect_maps:\s*\n((?:\s+\w+.*\n)*)", content
    )
    if not redirects_match:
        print("No redirects section found in mkdocs.yml")
        return {}

    redirects_text = redirects_match.group(1)
    redirects = {}

    # Parse each redirect line
    for line in redirects_text.strip().split("\n"):
        if ":" in line:
            # Extract key: value pairs
            parts = line.strip().split(":", 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                redirects[key] = value

    return redirects


def extract_supported_languages():
    """Extract supported languages from lang.yml"""
    lang_path = Path(__file__).parent.parent / "docs" / "assets" / "i18n-sites" / "lang.yml"

    with open(lang_path, "r", encoding="utf-8") as f:
        lang_data = yaml.safe_load(f)

    return [lang["locale"] for lang in lang_data]


def generate_js_redirects_object(redirects):
    """Generate JavaScript object from redirects"""
    js_lines = ["        const mkdocsRedirects = {"]

    for key, value in redirects.items():
        js_lines.append(f"            '{key}': '{value}',")

    js_lines.append("        };")
    return "\n".join(js_lines)


def update_404_html():
    """Update 404.html with current redirect mappings"""
    redirects = extract_redirects_from_mkdocs()
    languages = extract_supported_languages()

    print(f"Found {len(redirects)} redirect mappings")
    print(f"Supported languages: {languages}")

    # Generate JavaScript code
    js_redirects = generate_js_redirects_object(redirects)
    js_languages = f"        const supportedLanguages = {languages};"

    # Read current 404.html
    html_path = Path(__file__).parent.parent / "docs" / "overrides" / "404.html"
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the mkdocsRedirects object
    pattern1 = r"const mkdocsRedirects = \{[\s\S]*?\};"
    new_content = re.sub(pattern1, js_redirects, content)

    # Replace the supportedLanguages array
    pattern2 = r"const supportedLanguages = \[[\s\S]*?\];"
    new_content = re.sub(pattern2, js_languages, new_content)

    # Write back to file
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated {html_path}")
    print("Redirect mappings synced successfully!")


if __name__ == "__main__":
    update_404_html()
