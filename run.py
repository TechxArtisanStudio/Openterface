#!/usr/bin/env python3
import sys
import subprocess
import argparse
import os
import socket
from pathlib import Path

def get_repo_root():
    """Get the repository root directory (where mkdocs.yml is located)"""
    # Start from the directory containing this script
    current = Path(__file__).parent.resolve()
    
    # Look for mkdocs.yml in current directory or parents
    for path in [current] + list(current.parents):
        mkdocs_path = path / "mkdocs.yml"
        if mkdocs_path.exists() and mkdocs_path.is_file():
            return path
    
    # Fallback to script directory
    return current

def get_cms_script_path(script_relative_path):
    """Get full path to a script in openterface-cms/scripts/"""
    repo_root = get_repo_root()
    cms_scripts_dir = repo_root / "openterface-cms" / "scripts"
    script_path = cms_scripts_dir / script_relative_path
    
    if not script_path.exists():
        raise FileNotFoundError(
            f"Script not found: {script_path}\n"
            f"Make sure openterface-cms submodule is initialized:\n"
            f"  git submodule update --init --recursive"
        )
    
    return str(script_path)

def update_config(skip_versions=False):
    """Update mkdocs.yml with dynamic values"""
    script_path = get_cms_script_path("update_config.py")
    
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
    script_path = get_cms_script_path("update-post-tool/count_updates.py")
    
    cmd = [sys.executable, script_path]
    
    print("Counting update posts...")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Warning: Update count failed, continuing with existing config")
    return result.returncode == 0


def generate_updates_lists():
    """Generate automatic updates lists from H1 titles"""
    script_path = get_cms_script_path("update-post-tool/generate_updates_list.py")
    
    cmd = [sys.executable, script_path, "--update-files"]
    
    print("Generating updates lists...")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Warning: Updates list generation failed, continuing with existing lists")
    return result.returncode == 0


def manage_i18n(action, languages=None):
    """Manage i18n configuration in mkdocs.yml"""
    script_path = get_cms_script_path("manage_i18n.py")
    
    cmd = [sys.executable, script_path, action]
    if languages:
        cmd.extend(["--languages"] + languages)
    
    print(f"Managing i18n configuration: {action}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"Warning: i18n {action} failed, continuing with existing config")
    return result.returncode == 0


def get_local_ip():
    """Get the local IP address for network access"""
    try:
        # Connect to a remote address to determine local IP
        # This doesn't actually send data, just determines the route
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        # Fallback: try to get hostname IP
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        except Exception:
            return None

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
    parser.add_argument('--local-network', action='store_true',
                       help='Serve on local network (sets host to 0.0.0.0 and displays local IP address)')
    parser.add_argument('--i18n', choices=['add', 'remove', 'list'], 
                       help='Manage i18n configuration: add all languages, remove all except English, or list current languages')
    parser.add_argument('--lang', nargs='+',
                       help='Specific languages to add/remove when using --i18n (e.g., zh ja ko)')
    
    args = parser.parse_args()
    
    # Handle local network flag
    local_ip = None
    if args.local_network:
        args.host = '0.0.0.0'
        local_ip = get_local_ip()
        if local_ip:
            print(f"\n{'='*60}")
            print(f"🌐 Serving on local network")
            print(f"{'='*60}")
            print(f"📍 EXACT IP ADDRESS TO VISIT:")
            print(f"   http://{local_ip}:{args.port}")
            print(f"{'='*60}")
            print(f"📱 Use this URL on your phone: http://{local_ip}:{args.port}")
            print(f"💻 Use this URL locally: http://localhost:{args.port}")
            print(f"{'='*60}\n")
        else:
            print("\n⚠️  Could not determine local IP address")
            print(f"   Serving on 0.0.0.0:{args.port} - check your network settings for the IP\n")
    
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
    if args.local_network and local_ip:
        print(f"\n{'='*60}")
        print(f"🌐 Server is starting...")
        print(f"📍 VISIT THE WEBSITE AT: http://{local_ip}:{args.port}")
        print(f"{'='*60}\n")
    subprocess.run(cmd)

if __name__ == "__main__":
    main()