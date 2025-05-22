import sys
import yaml
from bs4 import BeautifulSoup

def update_html_translation(html_path, translations_path, target_lang, output_path):
    print(f"Updating translations for {html_path} to {target_lang}")
    # Load translations from YAML
    with open(translations_path, 'r', encoding='utf-8') as f:
        translations = yaml.safe_load(f)

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

    # Parse HTML
    soup = BeautifulSoup(html_text, "html.parser")

    # Replace text for elements with a matching key attribute
    for key, lang_map in translation_map.items():
        print(f"Processing key: {key}")
        if not isinstance(lang_map, dict) or target_lang not in lang_map:
            print(f"Key '{key}' not found in translation map or target language '{target_lang}' not available.")
            print(lang_map)
            continue
        translated = lang_map[target_lang]
        print(f"Translating key '{key}' to '{translated}'")
        # Split translation by '|||'
        translated_parts = translated.split('|||')
        # Find all elements with key attribute matching this key
        for tag in soup.find_all(attrs={"data-i18n": key}):
            # Skip tags where any attribute contains Jinja/templating
            if any('{{' in str(val) or '}}' in str(val) for val in tag.attrs.values()):
                continue
            old_text = tag.text
            # If only one part, replace the whole text
            if len(translated_parts) == 1:
                tag.string = translated
            else:
                # Remove all children and insert each part as a NavigableString, separated by <br/>
                tag.clear()
                for idx, part in enumerate(translated_parts):
                    tag.append(part)
                    if idx < len(translated_parts) - 1:
                        tag.append(soup.new_tag("br"))
            print(f"Translated key '{key}': '{old_text}' -> '{translated}'")

    # Write back the modified HTML to the specified output path
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_translations.py <input_html_file> <target_lang> <output_html_file>")
        sys.exit(1)
    html_file = sys.argv[1]
    translation_yml = 'translations/lang.yml'
    target_lang = sys.argv[2]
    output_html = sys.argv[3]
    update_html_translation(html_file, translation_yml, target_lang, output_html)