from bs4 import BeautifulSoup
import sys
import json
import re
import os
import yaml

def tag_visible(element):
    from bs4.element import Comment
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def is_template_placeholder(text):
    # Skip Jinja or similar template placeholders: {{ ... }} or {% ... %}
    return re.search(r"{{.*?}}|{%.*?%}", text)

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(string=True)
    visible_texts = [
        t.strip() for t in texts
        if tag_visible(t) and t.strip() and not is_template_placeholder(t)
    ]
    return visible_texts

def get_lang_from_mkdocs_yml(yml_path):
    try:
        with open(yml_path, encoding='utf-8') as f:
            mkdocs = yaml.safe_load(f)
        # Try both 'lang' and 'locale'
        lang = mkdocs.get('lang') or mkdocs.get('locale') or 'en'
        # Only keep the language code (e.g., 'en' from 'en-US')
        return lang.split('-')[0]
    except Exception:
        return 'en'

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_visible_text.py <html_file> <mkdocs.yml>")
        sys.exit(1)
    html_file = sys.argv[1]
    mkdocs_yml = sys.argv[2]
    lang = get_lang_from_mkdocs_yml(mkdocs_yml)
    with open(html_file, encoding='utf-8') as f:
        html = f.read()
    visible_texts = text_from_html(html)

    # Use the html_file path relative to the project root as the key
    project_root = '.'
    rel_html_path = os.path.relpath(html_file, project_root)
    rel_html_path = rel_html_path.replace("\\", "/")  # For Windows compatibility

    new_dict = {rel_html_path: {text: text for text in visible_texts}}

    # Set output path to translations/{lang}.json
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'translations')
    output_dir = os.path.abspath(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    output_json = os.path.join(output_dir, f"{lang}.json")

    # Read existing translations
    existing_dict = {}
    if os.path.exists(output_json):
        with open(output_json, 'r', encoding='utf-8') as f:
            try:
                existing_dict = json.load(f)
            except Exception:
                print(f"Warning: Could not parse existing {output_json}, will overwrite.")

    # Compare and warn about changes
    changed = False
    changed_keys = []
    removed_keys = []
    existing_file_dict = existing_dict.get(rel_html_path, {}) if existing_dict else {}
    for key, value in new_dict[rel_html_path].items():
        if key not in existing_file_dict or existing_file_dict[key] != value:
            changed = True
            changed_keys.append(key)
    removed_keys = [k for k in existing_file_dict if k not in new_dict[rel_html_path]]
    if changed or removed_keys:
        print("Warning: The following translation keys have changed or are new:")
        for k in changed_keys:
            print(f"  Added/Changed: {k}")
        for k in removed_keys:
            print(f"  Removed: {k}")

    # Merge new_dict into existing_dict
    existing_dict[rel_html_path] = new_dict[rel_html_path]
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(existing_dict, f, ensure_ascii=False, indent=2)
    print(f"Translation JSON written to {output_json}")