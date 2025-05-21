import os
import subprocess
import sys

def update_translations_in_folder(folder_path):
    """
    Recursively find all .po files under the given folder and update their translations using msgmerge.
    Assumes that for each .po file, a corresponding .pot template exists in the same directory.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.po'):
                po_path = os.path.join(root, file)
                pot_path = os.path.join(root, file[:-3] + '.pot')
                if os.path.exists(pot_path):
                    print(f"Updating {po_path} with {pot_path} ...")
                    subprocess.run(['msgmerge', '--update', '--backup=none', po_path, pot_path], check=True)
                else:
                    print(f"Template {pot_path} not found for {po_path}, skipping.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_all_translations.py <folder_path>")
        sys.exit(1)
    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"Error: {folder} is not a valid directory.")
        sys.exit(1)
    update_translations_in_folder(folder)