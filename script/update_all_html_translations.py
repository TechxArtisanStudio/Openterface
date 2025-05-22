import os
import sys
from update_translations import update_html_translation

def translate_all_html(folder, translations_path, target_lang, output_folder):
    for root, dirs, files in os.walk(folder):
        # Skip any folder named 'partials'
        if 'partials' in dirs:
            dirs.remove('partials')
        for file in files:
            if file.endswith('.html'):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(input_path, folder)
                output_path = os.path.join(output_folder, rel_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                update_html_translation(input_path, translations_path, target_lang, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_all_html_translations.py <input_folder> <target_lang> <output_folder>")
        sys.exit(1)
    input_folder = sys.argv[1]
    target_lang = sys.argv[2]
    output_folder = sys.argv[3]
    translations_path = 'translations/lang.yml'
    translate_all_html(input_folder, translations_path, target_lang, output_folder)