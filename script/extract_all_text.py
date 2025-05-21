import os
import sys
import subprocess

def find_html_files(folder):
    html_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_all_text.py <html_folder> <mkdocs.yml>")
        sys.exit(1)
    html_folder = sys.argv[1]
    mkdocs_yml = sys.argv[2]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    extract_script = os.path.join(script_dir, "extract_visible_text.py")

    html_files = find_html_files(html_folder)
    for html_file in html_files:
        print(f"Processing: {html_file}")
        subprocess.run([sys.executable, extract_script, html_file, mkdocs_yml])