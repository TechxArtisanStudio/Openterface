#!/usr/bin/env python3
"""
Unified build preparation script for MkDocs site.

Handles all pre-build steps:
- Update mkdocs config
- Manage updates (count and generate lists)
- Sync languages (full i18n or English-only)
- Generate static i18n pages (only for full i18n mode)
- Copy .well-known directory (for CI/CD)
- Execute action (build or serve)

Usage:
    # CI/CD - Full i18n build
    python scripts/prepare_build.py --i18n-mode full --copy-well-known --action build
    
    # Local - English only (fast)
    python scripts/prepare_build.py --i18n-mode en-only --action serve
    
    # Local - Full i18n (for testing)
    python scripts/prepare_build.py --i18n-mode full --action serve
    
    # Local - Full i18n on local network
    python scripts/prepare_build.py --i18n-mode full --action serve --local-network
"""

import argparse
import os
import shutil
import socket
import subprocess
import sys
from pathlib import Path


def get_local_ip():
    """Get the local IP address for network access."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        except Exception:
            return None


def run_command(cmd, description, continue_on_error=False):
    """Run a command and return success status."""
    print(f"\n{'='*60}")
    print(f"🔄 {description}")
    print(f"{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    
    result = subprocess.run(cmd)
    success = result.returncode == 0
    
    if success:
        print(f"✅ {description} - Success")
    else:
        if continue_on_error:
            print(f"⚠️  {description} - Warning (continuing)")
        else:
            print(f"❌ {description} - Failed")
    
    return success


def update_config(skip_versions=False):
    """Update mkdocs.yml with dynamic values."""
    script_path = os.path.join(os.path.dirname(__file__), "update_config.py")
    cmd = [sys.executable, script_path]
    
    if skip_versions:
        cmd.append("--skip-versions")
    
    return run_command(cmd, "Update mkdocs config with dynamic values", continue_on_error=True)


def manage_updates():
    """Count update posts and generate update lists."""
    script_path = os.path.join(os.path.dirname(__file__), "update-post-tool", "manage_updates.py")
    cmd = [sys.executable, script_path]
    
    return run_command(cmd, "Manage updates (count and generate lists)", continue_on_error=True)


def sync_languages(i18n_mode):
    """Sync languages based on mode."""
    script_path = os.path.join(os.path.dirname(__file__), "manage_i18n.py")
    
    if i18n_mode == "full":
        cmd = [sys.executable, script_path, "add"]
        description = "Add all languages to mkdocs config"
    elif i18n_mode == "en-only":
        cmd = [sys.executable, script_path, "remove"]
        description = "Remove all languages except English"
    else:
        print(f"❌ Invalid i18n-mode: {i18n_mode}")
        return False
    
    return run_command(cmd, description, continue_on_error=False)


def generate_static_i18n_pages():
    """Generate static i18n pages (home, videos, hreflang)."""
    script_path = os.path.join(os.path.dirname(__file__), "i18n-site-tools", "generate_all_i18n.py")
    cmd = [sys.executable, script_path]
    
    return run_command(cmd, "Generate static i18n pages", continue_on_error=False)


def copy_well_known():
    """Copy .well-known directory to site/.well-known."""
    project_root = Path(__file__).parent.parent
    source_dir = project_root / "docs" / ".well-known"
    target_dir = project_root / "site" / ".well-known"
    
    if not source_dir.exists():
        print(f"⚠️  Source directory not found: {source_dir}")
        return True  # Not critical, continue
    
    print(f"\n{'='*60}")
    print(f"🔄 Copy .well-known directory")
    print(f"{'='*60}")
    
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
        print(f"✅ Copied .well-known directory to {target_dir}")
        return True
    except Exception as e:
        print(f"❌ Failed to copy .well-known directory: {e}")
        return False


def run_mkdocs_build():
    """Run mkdocs build."""
    cmd = [sys.executable, "-m", "mkdocs", "build"]
    return run_command(cmd, "Build MkDocs site", continue_on_error=False)


def run_mkdocs_serve(host, port, local_network=False):
    """Run mkdocs serve."""
    cmd = [sys.executable, "-m", "mkdocs", "serve", "-a", f"{host}:{port}"]
    
    # Show local network info if requested
    if local_network:
        local_ip = get_local_ip()
        if local_ip:
            print(f"\n{'='*60}")
            print(f"🌐 Serving on local network")
            print(f"{'='*60}")
            print(f"📍 EXACT IP ADDRESS TO VISIT:")
            print(f"   http://{local_ip}:{port}")
            print(f"{'='*60}")
            print(f"📱 Use this URL on your phone: http://{local_ip}:{port}")
            print(f"💻 Use this URL locally: http://localhost:{port}")
            print(f"{'='*60}\n")
        else:
            print("\n⚠️  Could not determine local IP address")
            print(f"   Serving on {host}:{port} - check your network settings for the IP\n")
    
    print(f"\n{'='*60}")
    print(f"🚀 Starting MkDocs server...")
    print(f"{'='*60}\n")
    
    # Run serve (this blocks until interrupted)
    subprocess.run(cmd)


def main():
    parser = argparse.ArgumentParser(
        description="Unified build preparation script for MkDocs site",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--i18n-mode",
        choices=["full", "en-only"],
        default="full",
        help="i18n mode: 'full' (all languages) or 'en-only' (English only). Default: full"
    )
    
    parser.add_argument(
        "--skip-config",
        action="store_true",
        help="Skip updating mkdocs.yml with dynamic values"
    )
    
    parser.add_argument(
        "--skip-updates",
        action="store_true",
        help="Skip update counting and generation"
    )
    
    parser.add_argument(
        "--skip-static-pages",
        action="store_true",
        help="Skip static i18n page generation (only relevant for full i18n mode)"
    )
    
    parser.add_argument(
        "--copy-well-known",
        action="store_true",
        help="Copy .well-known directory to site/.well-known (for CI/CD)"
    )
    
    parser.add_argument(
        "--action",
        choices=["build", "serve"],
        default="serve",
        help="Action to execute: 'build' (for CI/CD) or 'serve' (for local). Default: serve"
    )
    
    parser.add_argument(
        "--port",
        default="8002",
        help="Port for serve mode (default: 8002)"
    )
    
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host for serve mode (default: 0.0.0.0)"
    )
    
    parser.add_argument(
        "--local-network",
        action="store_true",
        help="Show local network IP address (for local development)"
    )
    
    parser.add_argument(
        "--skip-versions",
        action="store_true",
        help="Skip fetching versions from APIs when updating config (faster)"
    )
    
    args = parser.parse_args()
    
    # Print header
    print("\n" + "="*60)
    print("🔧 MkDocs Build Preparation")
    print("="*60)
    print(f"i18n Mode: {args.i18n_mode}")
    print(f"Action: {args.action}")
    if args.action == "serve":
        print(f"Host: {args.host}")
        print(f"Port: {args.port}")
    print("="*60 + "\n")
    
    # Step 1: Update config
    if not args.skip_config:
        if not update_config(skip_versions=args.skip_versions):
            print("⚠️  Config update had issues, but continuing...")
    else:
        print("⏭️  Skipping config update")
    
    # Step 2: Manage updates
    if not args.skip_updates:
        if not manage_updates():
            print("⚠️  Update management had issues, but continuing...")
    else:
        print("⏭️  Skipping update management")
    
    # Step 3: Sync languages
    if not sync_languages(args.i18n_mode):
        print("❌ Language sync failed - aborting")
        sys.exit(1)
    
    # Step 4: Generate static i18n pages (only for full i18n mode)
    if args.i18n_mode == "full" and not args.skip_static_pages:
        if not generate_static_i18n_pages():
            print("❌ Static i18n page generation failed - aborting")
            sys.exit(1)
    elif args.i18n_mode == "en-only":
        print("⏭️  Skipping static i18n page generation (English-only mode)")
    else:
        print("⏭️  Skipping static i18n page generation (--skip-static-pages)")
    
    # Step 5: Copy .well-known (only if requested)
    if args.copy_well_known:
        if not copy_well_known():
            print("⚠️  .well-known copy had issues, but continuing...")
    else:
        print("⏭️  Skipping .well-known copy")
    
    # Step 6: Execute action
    print("\n" + "="*60)
    print(f"✅ All preparation steps completed!")
    print("="*60 + "\n")
    
    if args.action == "build":
        if not run_mkdocs_build():
            print("❌ MkDocs build failed")
            sys.exit(1)
        print("\n✅ Build completed successfully!")
    elif args.action == "serve":
        run_mkdocs_serve(args.host, args.port, args.local_network)
        # Note: serve blocks, so we never reach here unless interrupted


if __name__ == "__main__":
    main()

