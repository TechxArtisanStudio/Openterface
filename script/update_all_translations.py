import os
import sys
from update_translations import update_html_translation

def update_all_html_translations(source_folder, lang, output_folder):
    translations_path = 'translations/lang.yml'
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.html'):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, source_folder)
                output_path = os.path.join(output_folder, rel_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                update_html_translation(input_path, translations_path, lang, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_all_translations.py <source_folder> <lang> <output_folder>")
        sys.exit(1)
    source_folder = sys.argv[1]
    lang = sys.argv[2]
    output_folder = sys.argv[3]
    if not os.path.isdir(source_folder):
        print(f"Error: {source_folder} is not a valid directory.")
        sys.exit(1)
    update_all_html_translations(source_folder, lang, output_folder)