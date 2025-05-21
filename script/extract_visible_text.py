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
    visible_texts = []
    for t in texts:
        if tag_visible(t) and t.strip() and not is_template_placeholder(t):
            parent = t.parent
            data_id = parent.attrs.get('data-i18n') if parent and parent.has_attr('data-i18n') else None
            visible_texts.append({'text': t.strip(), 'id': data_id})
    return visible_texts

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_visible_text.py <html_file> <lang>")
        sys.exit(1)
    html_file = sys.argv[1]
    lang = sys.argv[2]
    with open(html_file, encoding='utf-8') as f:
        html = f.read()
    visible_texts = text_from_html(html)

    # Set output path to translations/{lang}.yml
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'translations')
    output_dir = os.path.abspath(output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    output_yaml = os.path.join(output_dir, f"{lang}.yml")

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
        for key, entry in entries.items():
            if isinstance(entry, dict) and 'id' in entry:
                global_id_lookup[entry['id']] = (parent_node, key, entry)

    def build_entry(item, prev_entry=None):
        entry = {}
        if item['id'] is not None:
            entry['id'] = item['id']
        entry['original'] = item['text']
        # Preserve previous translateto if exists, else empty string
        if prev_entry and 'translateto' in prev_entry:
            entry['translateto'] = prev_entry['translateto']
        else:
            entry['translateto'] = ""
        return entry

    # Prepare previous entries for merging
    existing_file_dict = existing_dict.get(rel_html_path, {}) if existing_dict else {}

    new_entries = {}
    for item in visible_texts:
        prev_entry = None
        # 1. Check if id exists globally (in any parent node)
        if item['id'] and item['id'] in global_id_lookup:
            parent_node, key, entry = global_id_lookup[item['id']]
            # If parent node is different, update only the 'original' in the existing parent node
            if parent_node != rel_html_path:
                entry['original'] = item['text']
                continue  # Do not add to new_entries for this file
            else:
                prev_entry = entry
        # 2. Else, check if text exists in current file
        elif item['text'] in existing_file_dict:
            prev_entry = existing_file_dict[item['text']]
        # 3. Build entry for this file if not handled above
        new_entries[item['text']] = build_entry(item, prev_entry)

    # Update the current file's entries
    new_dict = existing_dict.copy()
    new_dict[rel_html_path] = new_entries

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
    with open(output_yaml, 'w', encoding='utf-8') as f:
        yaml.dump(existing_dict, f, allow_unicode=True, sort_keys=False)
    print(f"Translation YAML written to {output_yaml}")