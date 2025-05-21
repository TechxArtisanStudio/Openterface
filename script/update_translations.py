import sys
import json
import re

def update_html_translation(html_path, translations_path, target_lang):
    # Load translations
    with open(translations_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Find the translation map for this HTML file
    html_key = None
    for key in translations.keys():
        if html_path.endswith(key):
            html_key = key
            break
    if not html_key:
        print(f"No translations found for {html_path} in {translations_path}")
        return

    translation_map = translations[html_key]

    # Read HTML as text
    with open(html_path, 'r', encoding='utf-8') as f:
        html_text = f.read()

    # Function to replace text between tags
    def replace_text(match):
        text = match.group(1)
        stripped = text.strip()
        if stripped in translation_map and stripped != "":
            leading = text[:len(text) - len(text.lstrip())]
            trailing = text[len(text.rstrip()):]
            return f">{leading}{translation_map[stripped]}{trailing}<"
        return match.group(0)

    # Regex to find text between tags (not inside tags)
    pattern = re.compile(r'>([^<]+)<')
    new_html = pattern.sub(replace_text, html_text)

    # Write back the modified HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_translations.py <html_file> <translation_json> <target_lang>")
        sys.exit(1)
    html_file = sys.argv[1]
    translation_json = sys.argv[2]
    target_lang = sys.argv[3]
    update_html_translation(html_file, translation_json, target_lang)