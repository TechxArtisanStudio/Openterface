#!/usr/bin/env python3
import sys
import subprocess
import argparse
import os

def update_config(skip_versions=False):
    """Update mkdocs.yml with dynamic values"""
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "update_config.py")
    
    cmd = [sys.executable, script_path]
    if skip_versions:
        cmd.append("--skip-versions")
    
    print("Updating mkdocs config...")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Warning: Config update failed, continuing with existing config")
    return result.returncode == 0


def count_updates():
    """Count update posts and update mkdocs.yml with product update variables"""
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "count_updates.py")
    
    cmd = [sys.executable, script_path]
    
    print("Counting update posts...")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Warning: Update count failed, continuing with existing config")
    return result.returncode == 0


def generate_updates_lists():
    """Generate automatic updates lists from H1 titles"""
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "generate_updates_list.py")
    
    cmd = [sys.executable, script_path, "--update-files"]
    
    print("Generating updates lists...")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Warning: Updates list generation failed, continuing with existing lists")
    return result.returncode == 0


def manage_i18n(action, languages=None):
    """Manage i18n configuration in mkdocs.yml"""
    script_path = os.path.join(os.path.dirname(__file__), "scripts", "manage_i18n.py")
    
    cmd = [sys.executable, script_path, action]
    if languages:
        cmd.extend(["--languages"] + languages)
    
    print(f"Managing i18n configuration: {action}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"Warning: i18n {action} failed, continuing with existing config")
    return result.returncode == 0

def main():
    parser = argparse.ArgumentParser(description='Run MkDocs serve with config updates')
    parser.add_argument('--no-update-config', action='store_true',
                       help='Skip updating mkdocs.yml with dynamic values (config updates are enabled by default)')
    parser.add_argument('--fetch-versions', action='store_true',
                       help='Fetch latest versions from APIs when updating config (slower but gets latest versions)')
    parser.add_argument('--port', default='8002',
                       help='Port to serve on (default: 8002)')
    parser.add_argument('--host', default='0.0.0.0',
                       help='Host to bind to (default: 0.0.0.0)')
    parser.add_argument('--i18n', choices=['add', 'remove', 'list'], 
                       help='Manage i18n configuration: add all languages, remove all except English, or list current languages')
    parser.add_argument('--lang', nargs='+',
                       help='Specific languages to add/remove when using --i18n (e.g., zh ja ko)')
    
    args = parser.parse_args()
    
    # Handle i18n management
    if args.i18n:
        if args.i18n == 'list':
            manage_i18n('list')
            return
        else:
            manage_i18n(args.i18n, args.lang)
    
    # Update config by default (unless explicitly disabled)
    if not args.no_update_config:
        skip_versions = not args.fetch_versions  # Skip versions unless explicitly requested
        update_config(skip_versions=skip_versions)
        count_updates()  # Always count updates when config is updated
        generate_updates_lists()  # Always generate updates lists when config is updated
    
    # Run mkdocs serve
    cmd = [
        sys.executable,    # ensures we use the current venv's Python
        "-m", "mkdocs",
        "serve",
        "-a", f"{args.host}:{args.port}"
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd)

if __name__ == "__main__":
    main()