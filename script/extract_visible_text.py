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

def extract_direct_text_blocks(element):
    """Extract direct text blocks from an element, separated by child tags."""
    blocks = []
    for child in element.children:
        if isinstance(child, str):
            text = child.strip()
            if text:
                blocks.append(text)
        elif hasattr(child, 'attrs') and child.has_attr('data-i18n'):
            # Skip child elements with data-i18n (they will be handled separately)
            continue
    return blocks

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    visible_texts = []

    # Find all elements with data-i18n
    for el in soup.find_all(attrs={"data-i18n": True}):
        blocks = extract_direct_text_blocks(el)
        if blocks:
            visible_texts.append({
                'text': '|||'.join(blocks),
                'id': el.attrs.get('data-i18n')
            })

    # Find all visible text nodes not inside a data-i18n element
    def is_inside_data_i18n(element):
        while element:
            if hasattr(element, 'attrs') and element.has_attr('data-i18n'):
                return True
            element = element.parent
        return False

    for t in soup.find_all(string=True):
        if tag_visible(t) and t.strip() and not is_template_placeholder(t):
            parent = t.parent
            if parent and parent.has_attr('data-i18n'):
                continue  # Already handled above
            if not is_inside_data_i18n(parent):
                visible_texts.append({'text': t.strip(), 'id': None})

    return visible_texts

def make_safe_key(text):
    # Replace spaces with underscores, remove non-alphanumeric except underscores
    return re.sub(r'[^A-Za-z0-9_]', '', text.replace(' ', '_'))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_visible_text.py <html_file>")
        sys.exit(1)
    html_file = sys.argv[1]
    with open(html_file, encoding='utf-8') as f:
        html = f.read()
    visible_texts = text_from_html(html)

    # Set output path to translations/lang.yml
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'translations')
    output_dir = os.path.abspath(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    output_yaml = os.path.join(output_dir, f"lang.yml")

    # Read existing translations
    existing_dict = {}
    if os.path.exists(output_yaml):
        with open(output_yaml, 'r', encoding='utf-8') as f:
            try:
                existing_dict = yaml.safe_load(f) or {}
            except Exception:
                print(f"Warning: Could not parse existing {output_yaml}, will overwrite.")

    # Use the html_file path relative to the project root as the key
    project_root = '.'
    rel_html_path = os.path.relpath(html_file, project_root)
    rel_html_path = rel_html_path.replace("\\", "/")  # For Windows compatibility

    # Build a global id -> (parent_node, key, entry) mapping from all parent nodes
    global_id_lookup = {}
    for parent_node, entries in existing_dict.items():
        if not isinstance(entries, dict) or not entries:
            continue
        for key, entry in entries.items():
            if isinstance(entry, dict) and 'id' in entry:
                global_id_lookup[entry['id']] = (parent_node, key, entry)

    def build_entry(item, prev_entry=None):
        entry = {}
        entry['en'] = item['text']
        # Supported languages
        langs = ['de', 'es', 'fr', 'it', 'jp', 'ko', 'pt', 'ro', 'zh']
        for lang in langs:
            # Preserve previous translation if exists, else empty string
            if prev_entry and lang in prev_entry:
                entry[lang] = prev_entry[lang]
            else:
                entry[lang] = ""
        return entry

    # Prepare previous entries for merging
    existing_file_dict = existing_dict.get(rel_html_path) or {}

    new_entries = {}
    for item in visible_texts:
        prev_entry = None
        # 1. Check if id exists globally (in any parent node)
        key = item['id'] if item['id'] else make_safe_key(item['text'])
        if item['id'] and item['id'] in global_id_lookup:
            parent_node, _, entry = global_id_lookup[item['id']]
            prev_entry = entry
        elif key in existing_dict:
            prev_entry = existing_dict[key]
        new_entries[key] = build_entry(item, prev_entry)

    # Nest translations under the HTML file path
    new_dict = existing_dict.copy()
    new_dict[rel_html_path] = new_entries

    # Compare and warn about changes
    changed = False
    changed_keys = []
    removed_keys = []
    for key, value in new_entries.items():
        if key not in existing_dict or existing_dict[key] != value:
            changed = True
            changed_keys.append(key)
    removed_keys = [k for k in existing_dict if k not in new_entries and k not in [rel_html_path]]
    if changed or removed_keys:
        print("Warning: The following translation keys have changed or are new:")
        for k in changed_keys:
            print(f"  Added/Changed: {k}")
        for k in removed_keys:
            print(f"  Removed: {k}")

    # Write to YAML
    with open(output_yaml, 'w', encoding='utf-8') as f:
        yaml.dump(new_dict, f, allow_unicode=True, sort_keys=False)
    print(f"Translation YAML written to {output_yaml}")