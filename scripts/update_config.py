#!/usr/bin/env python3
"""
Script to update mkdocs.yml with dynamic values like versions and copyright year.
Can be used by both GitHub Actions and local development.
"""

import os
import sys
import re
import argparse
import subprocess
from datetime import datetime


def get_qt_version():
    """Get the latest QT version from GitHub API"""
    try:
        result = subprocess.run([
            'curl', '-sL', 
            'https://api.github.com/repos/TechxArtisanStudio/Openterface_QT/releases/latest'
        ], capture_output=True, text=True, check=True)
        
        # Extract version from JSON response
        match = re.search(r'"tag_name":\s*"([^"]+)"', result.stdout)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: Could not fetch QT version, using fallback", file=sys.stderr)
    
    return "v1.0.0"  # Fallback version


def get_android_version():
    """Get the latest Android version from GitHub API"""
    try:
        result = subprocess.run([
            'curl', '-sL', 
            'https://api.github.com/repos/TechxArtisanStudio/Openterface_Android/releases/latest'
        ], capture_output=True, text=True, check=True)
        
        # Extract version from JSON response
        match = re.search(r'"tag_name":\s*"([^"]+)"', result.stdout)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: Could not fetch Android version, using fallback", file=sys.stderr)
    
    return "v1.0.0"  # Fallback version


def get_macos_version():
    """Get the macOS version from App Store"""
    try:
        result = subprocess.run([
            'curl', '-sL', 
            'https://apps.apple.com/us/app/openterface-mini-kvm/id6478481082'
        ], capture_output=True, text=True, check=True)
        
        # Extract version from HTML response
        match = re.search(r'Version v*([0-9]+\.[0-9]+)', result.stdout)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: Could not fetch macOS version, using fallback", file=sys.stderr)
    
    return "1.0.0"  # Fallback version


def get_current_year():
    """Get the current year"""
    return datetime.now().year


def update_mkdocs_config(mkdocs_path="mkdocs.yml", 
                        qt_version=None, 
                        android_version=None, 
                        macos_version=None, 
                        copyright_year=None,
                        minikvm_purchase_link=None,
                        skip_versions=False):
    """
    Update mkdocs.yml with dynamic values
    
    Args:
        mkdocs_path: Path to mkdocs.yml file
        qt_version: QT version to set (if None, will fetch from API unless skip_versions=True)
        android_version: Android version to set (if None, will fetch from API unless skip_versions=True)
        macos_version: macOS version to set (if None, will fetch from API unless skip_versions=True)
        copyright_year: Copyright year to set (if None, will use current year)
        minikvm_purchase_link: Mini-KVM purchase link to set (if None, will keep existing value)
        skip_versions: If True, skip fetching versions from APIs
    """
    
    # Read the current mkdocs.yml
    try:
        with open(mkdocs_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {mkdocs_path} not found", file=sys.stderr)
        return False
    
    # Get values
    if not skip_versions:
        if qt_version is None:
            qt_version = get_qt_version()
        if android_version is None:
            android_version = get_android_version()
        if macos_version is None:
            macos_version = get_macos_version()
    
    if copyright_year is None:
        copyright_year = get_current_year()
    
    # Find the extra: section and remove existing dynamic entries
    lines = content.split('\n')
    new_lines = []
    in_extra_section = False
    skip_next_lines = 0
    
    for i, line in enumerate(lines):
        if skip_next_lines > 0:
            skip_next_lines -= 1
            continue
            
        # Check if we're entering the extra: section
        if line.strip() == 'extra:':
            in_extra_section = True
            new_lines.append(line)
            continue
        
        # If we're in the extra section, check for existing dynamic entries to replace
        if in_extra_section:
            # Check if this line is a dynamic entry we want to replace
            should_replace = False
            if line.strip().startswith('qt_version:') and not skip_versions:
                should_replace = True
            elif line.strip().startswith('android_version:') and not skip_versions:
                should_replace = True
            elif line.strip().startswith('macos_version:') and not skip_versions:
                should_replace = True
            elif line.strip().startswith('copyright_year:'):
                should_replace = True
            elif minikvm_purchase_link is not None and line.strip().startswith('minikvm_purchase_link:'):
                should_replace = True
            
            if should_replace:
                continue  # Skip this line, we'll add new ones
        
        # If we hit a non-indented line and we were in extra section, we're done
        if in_extra_section and line and not line.startswith(' ') and not line.startswith('\t'):
            in_extra_section = False
        
        new_lines.append(line)
    
    # Find where to insert the new entries (right after 'extra:')
    insert_index = -1
    for i, line in enumerate(new_lines):
        if line.strip() == 'extra:':
            insert_index = i + 1
            break
    
    if insert_index == -1:
        print("Error: Could not find 'extra:' section in mkdocs.yml", file=sys.stderr)
        return False
    
    # Insert the new entries
    entries_to_insert = []
    if not skip_versions:
        entries_to_insert.extend([
            f"  qt_version: {qt_version}",
            f"  android_version: {android_version}",
            f"  macos_version: {macos_version}"
        ])
    entries_to_insert.append(f"  copyright_year: {copyright_year}")
    
    # Add minikvm_purchase_link if provided
    if minikvm_purchase_link is not None:
        entries_to_insert.append(f"  minikvm_purchase_link: {minikvm_purchase_link}")
    
    # Insert the entries
    for entry in reversed(entries_to_insert):
        new_lines.insert(insert_index, entry)
    
    # Write the updated content
    try:
        with open(mkdocs_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"Successfully updated {mkdocs_path}")
        if not skip_versions:
            print(f"  QT Version: {qt_version}")
            print(f"  Android Version: {android_version}")
            print(f"  macOS Version: {macos_version}")
        print(f"  Copyright Year: {copyright_year}")
        if minikvm_purchase_link is not None:
            print(f"  Mini-KVM Purchase Link: {minikvm_purchase_link}")
        
        return True
    except Exception as e:
        print(f"Error writing to {mkdocs_path}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Update mkdocs.yml with dynamic values')
    parser.add_argument('--mkdocs-path', default='mkdocs.yml', 
                       help='Path to mkdocs.yml file (default: mkdocs.yml)')
    parser.add_argument('--qt-version', 
                       help='QT version to set (if not provided, will fetch from API)')
    parser.add_argument('--android-version', 
                       help='Android version to set (if not provided, will fetch from API)')
    parser.add_argument('--macos-version', 
                       help='macOS version to set (if not provided, will fetch from API)')
    parser.add_argument('--copyright-year', type=int,
                       help='Copyright year to set (if not provided, will use current year)')
    parser.add_argument('--minikvm-purchase-link',
                       help='Mini-KVM purchase link to set (if not provided, will keep existing value)')
    parser.add_argument('--skip-versions', action='store_true',
                       help='Skip fetching versions from APIs (useful for local testing)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be updated without making changes')
    
    args = parser.parse_args()
    
    if args.dry_run:
        print("Dry run mode - would update with:")
        if not args.skip_versions:
            print(f"  QT Version: {args.qt_version or get_qt_version()}")
            print(f"  Android Version: {args.android_version or get_android_version()}")
            print(f"  macOS Version: {args.macos_version or get_macos_version()}")
        print(f"  Copyright Year: {args.copyright_year or get_current_year()}")
        return
    
    success = update_mkdocs_config(
        mkdocs_path=args.mkdocs_path,
        qt_version=args.qt_version,
        android_version=args.android_version,
        macos_version=args.macos_version,
        copyright_year=args.copyright_year,
        minikvm_purchase_link=args.minikvm_purchase_link,
        skip_versions=args.skip_versions
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
