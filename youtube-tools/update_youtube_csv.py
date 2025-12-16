#!/usr/bin/env python3
"""
YouTube CSV Metadata Updater

This script updates youtube-tools/youtube.csv with YouTube video metadata.
It fetches metadata for videos and updates the CSV file, preserving user edits
and supporting maintenance workflows.

Usage:
    python update_youtube_csv.py [--dry-run] [--verbose] [--offline] [--force] [--skip-existing]
"""

import os
import re
import sys
import csv
import time
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import requests
from datetime import datetime

class YouTubeMetadataFetcher:
    """Fetches YouTube video metadata using web scraping."""
    
    def __init__(self, offline_mode: bool = False, proxy: str = None):
        self.offline_mode = offline_mode
        if not offline_mode:
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            })
            
            # Set up proxy if provided
            if proxy:
                proxies = {
                    'http': proxy,
                    'https': proxy
                }
                self.session.proxies.update(proxies)
                
        self.cache = {}
        
    def extract_video_id(self, url: str) -> Optional[str]:
        """Extract video ID from YouTube URL."""
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([^&\n?#]+)',
            r'youtube\.com/watch\?.*v=([^&\n?#]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def fetch_video_metadata(self, video_id: str) -> Dict[str, str]:
        """Fetch video metadata from YouTube."""
        if video_id in self.cache:
            return self.cache[video_id]
            
        if self.offline_mode:
            empty_metadata = {
                'title': '',
                'author_name': '',
                'thumbnail_url': '',
                'date': '',
                'views': '',
                'description': ''
            }
            self.cache[video_id] = empty_metadata
            return empty_metadata
            
        try:
            # Try to get video info from oEmbed API first (no API key needed)
            oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
            response = self.session.get(oembed_url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                metadata = {
                    'title': data.get('title', ''),
                    'author_name': data.get('author_name', ''),
                    'thumbnail_url': data.get('thumbnail_url', ''),
                    'date': '',  # oEmbed doesn't provide date
                    'views': '',  # oEmbed doesn't provide views
                    'description': ''
                }
                
                # Try to get additional info from the video page
                self._fetch_additional_metadata(video_id, metadata)
                
                self.cache[video_id] = metadata
                return metadata
                
        except Exception as e:
            print(f"Warning: Could not fetch metadata for video {video_id}: {e}")
            
        # Return empty metadata if fetch fails
        empty_metadata = {
            'title': '',
            'author_name': '',
            'thumbnail_url': '',
            'date': '',
            'views': '',
            'description': ''
        }
        self.cache[video_id] = empty_metadata
        return empty_metadata
    
    def _fetch_additional_metadata(self, video_id: str, metadata: Dict[str, str]):
        """Try to fetch additional metadata from the video page."""
        try:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            response = self.session.get(video_url, timeout=15)
            
            if response.status_code == 200:
                content = response.text
                
                # Extract views using regex - store as actual number
                views_match = re.search(r'"viewCount":"(\d+)"', content)
                if views_match:
                    views = int(views_match.group(1))
                    metadata['views'] = str(views)  # Store as number, not formatted
                
                # Extract publish date
                date_match = re.search(r'"publishDate":"(\d{4}-\d{2}-\d{2})"', content)
                if not date_match:
                    # Try alternative date patterns
                    date_match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})', content)
                    if date_match:
                        date_str = date_match.group(1).split('T')[0]  # Extract just the date part
                    else:
                        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', content)
                        if date_match:
                            date_str = date_match.group(1)
                        else:
                            date_str = None
                else:
                    date_str = date_match.group(1)
                
                if date_str:
                    try:
                        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                        metadata['date'] = date_obj.strftime('%Y-%m-%d')  # Keep ISO format for CSV
                    except ValueError:
                        metadata['date'] = date_str
                
                # Extract channel avatar/icon instead of video thumbnail
                avatar_match = re.search(r'"channelThumbnail":\s*\{\s*"thumbnails":\s*\[.*?"url":\s*"([^"]+)"', content, re.DOTALL)
                if avatar_match:
                    metadata['thumbnail_url'] = avatar_match.group(1)
                
                # Try to extract description - handle escaped quotes properly
                # Pattern: "shortDescription":"...content..." where content can contain escaped quotes
                # We need to match the full JSON string value, handling escaped quotes
                desc_patterns = [
                    # Try to find shortDescription in JSON structure
                    r'"shortDescription":"((?:[^"\\]|\\.)*)"',
                    # Alternative: look for description in videoPrimaryInfoRenderer
                    r'"description":\s*\{\s*"simpleText":\s*"((?:[^"\\]|\\.)*)"',
                    # Another alternative pattern
                    r'"description":\s*"((?:[^"\\]|\\.)*)"',
                ]
                
                description = ''
                for pattern in desc_patterns:
                    desc_match = re.search(pattern, content, re.DOTALL)
                    if desc_match:
                        description = desc_match.group(1)
                        # Unescape JSON sequences
                        description = description.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
                        # Replace newlines with spaces for CSV (or keep them - CSV can handle them)
                        description = description.replace('\n', ' ').replace('\r', ' ')
                        # Remove extra whitespace
                        description = ' '.join(description.split())
                        if description:
                            break
                
                if description:
                    metadata['description'] = description
                        
        except Exception as e:
            # Silently fail for additional metadata
            pass


class YouTubeCSVUpdater:
    """Updates YouTube CSV file with metadata."""
    
    CSV_COLUMNS = ['youtube_url', 'title', 'author_name', 'thumbnail_url', 'date', 'views', 'description', 'fetch_date', 'z_index', 'language', 'product', 'type']
    
    def __init__(self, csv_path: Path, dry_run: bool = False, verbose: bool = False, 
                 offline: bool = False, proxy: str = None, force: bool = False, 
                 skip_existing: bool = False):
        self.csv_path = csv_path
        self.dry_run = dry_run
        self.verbose = verbose
        self.offline = offline
        self.force = force
        self.skip_existing = skip_existing
        self.metadata_fetcher = YouTubeMetadataFetcher(offline_mode=offline, proxy=proxy)
        
    def normalize_views(self, views_str: str) -> str:
        """Convert formatted view count (e.g., '4.0K', '26.5K', '1.62M') to actual number."""
        if not views_str or not views_str.strip():
            return ''
        
        views_str = views_str.strip().upper()
        
        # If it's already a number, return as is
        if views_str.isdigit():
            return views_str
        
        # Handle K (thousands) and M (millions)
        try:
            if views_str.endswith('K'):
                number = float(views_str[:-1])
                return str(int(number * 1000))
            elif views_str.endswith('M'):
                number = float(views_str[:-1])
                return str(int(number * 1000000))
            elif views_str.endswith('B'):
                number = float(views_str[:-1])
                return str(int(number * 1000000000))
            else:
                # Try to parse as number
                return str(int(float(views_str)))
        except (ValueError, AttributeError):
            # If parsing fails, return original
            return views_str
    
    def read_csv(self) -> List[Dict[str, str]]:
        """Read CSV file and return list of rows."""
        rows = []
        
        if not self.csv_path.exists():
            print(f"Error: CSV file not found: {self.csv_path}")
            return rows
            
        try:
            with open(self.csv_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalize keys (remove BOM if present)
                    normalized_row = {}
                    for key, value in row.items():
                        normalized_key = key.lstrip('\ufeff')  # Remove BOM from key
                        normalized_row[normalized_key] = value
                    
                    # Normalize views column if present
                    if 'views' in normalized_row:
                        normalized_row['views'] = self.normalize_views(normalized_row['views'])
                    
                    # Skip rows where youtube_url is empty or is the header
                    url = normalized_row.get('youtube_url', '').strip()
                    if url and url != 'youtube_url':  # Skip header row if somehow included
                        rows.append(normalized_row)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            
        return rows
    
    def write_csv(self, rows: List[Dict[str, str]]):
        """Write rows to CSV file."""
        if self.dry_run:
            print(f"[DRY RUN] Would write {len(rows)} rows to {self.csv_path}")
            return
            
        try:
            # Create backup
            backup_path = self.csv_path.with_suffix('.csv.backup')
            if self.csv_path.exists():
                import shutil
                shutil.copy2(self.csv_path, backup_path)
                if self.verbose:
                    print(f"Created backup: {backup_path}")
            
            # Write CSV (using utf-8-sig to maintain BOM if it existed)
            # Note: Python's csv module automatically handles long descriptions by escaping
            # quotes and special characters, so full descriptions can be stored safely
            
            # Determine all columns: start with standard columns, then add any extra columns from rows
            all_columns = list(self.CSV_COLUMNS)
            for row in rows:
                for key in row.keys():
                    if key not in all_columns:
                        all_columns.append(key)  # Preserve any extra columns (e.g., language, product, type)
            
            with open(self.csv_path, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=all_columns)
                writer.writeheader()
                writer.writerows(rows)
                
            print(f"Updated CSV file: {self.csv_path}")
            
        except Exception as e:
            print(f"Error writing CSV file: {e}")
            raise
    
    def needs_update(self, row: Dict[str, str]) -> bool:
        """Check if a row needs metadata update."""
        url = row.get('youtube_url', '').strip()
        if not url:
            return False
            
        # If force mode, always update
        if self.force:
            return True
            
        # If skip_existing mode, skip rows that have any metadata
        if self.skip_existing:
            has_metadata = any([
                row.get('title', '').strip(),
                row.get('author_name', '').strip(),
                row.get('thumbnail_url', '').strip(),
                row.get('date', '').strip(),
                row.get('views', '').strip()
            ])
            return not has_metadata
            
        # Default: update if missing critical fields (title or author_name)
        missing_critical = not row.get('title', '').strip() or not row.get('author_name', '').strip()
        return missing_critical
    
    def update_row(self, row: Dict[str, str], row_num: int = 0, total_rows: int = 0) -> Tuple[Dict[str, str], bool]:
        """Update a single row with fetched metadata. Returns (updated_row, success)."""
        url = row.get('youtube_url', '').strip()
        if not url:
            return row, False
            
        video_id = self.metadata_fetcher.extract_video_id(url)
        if not video_id:
            print(f"  [{row_num}/{total_rows}] ⚠️  Warning: Could not extract video ID from {url}")
            return row, False
            
        # Show progress
        progress_pct = int((row_num / total_rows) * 100) if total_rows > 0 else 0
        print(f"  [{row_num}/{total_rows}] ({progress_pct}%) Fetching metadata for video {video_id}...", end='', flush=True)
            
        metadata = self.metadata_fetcher.fetch_video_metadata(video_id)
        
        # Check if we got meaningful metadata
        has_title = bool(metadata.get('title', '').strip())
        has_author = bool(metadata.get('author_name', '').strip())
        success = has_title or has_author
        
        # Update row with fetched metadata
        # Only update empty fields unless force mode
        if self.force:
            # Force mode: overwrite all fields
            row['title'] = metadata.get('title', '')
            row['author_name'] = metadata.get('author_name', '')
            row['thumbnail_url'] = metadata.get('thumbnail_url', '')
            row['date'] = metadata.get('date', '')
            row['views'] = metadata.get('views', '')
            row['description'] = metadata.get('description', '')
        else:
            # Normal mode: only fill empty fields, preserve user edits
            if not row.get('title', '').strip():
                row['title'] = metadata.get('title', '')
            if not row.get('author_name', '').strip():
                row['author_name'] = metadata.get('author_name', '')
            if not row.get('thumbnail_url', '').strip():
                row['thumbnail_url'] = metadata.get('thumbnail_url', '')
            if not row.get('date', '').strip():
                row['date'] = metadata.get('date', '')
            if not row.get('views', '').strip():
                row['views'] = metadata.get('views', '')
            if not row.get('description', '').strip():
                row['description'] = metadata.get('description', '')
        
        # Update fetch_date if we fetched new data
        if metadata.get('title') or metadata.get('author_name'):
            row['fetch_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Show result
        if success:
            title_preview = metadata.get('title', '')[:50] + '...' if len(metadata.get('title', '')) > 50 else metadata.get('title', '')
            desc_len = len(metadata.get('description', ''))
            desc_info = f" (desc: {desc_len} chars)" if desc_len > 0 else ""
            print(f" ✓ {title_preview}{desc_info}")
        else:
            print(f" ✗ Failed to fetch metadata")
        
        return row, success
    
    def update_csv(self):
        """Update CSV file with metadata."""
        print("=" * 60)
        print("YouTube CSV Metadata Updater")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
            
        total_rows = len(rows)
        print(f"\n📊 Found {total_rows} rows in CSV file.")
        
        # Count rows that need updating
        rows_to_update = [i for i, row in enumerate(rows) if self.needs_update(row)]
        rows_to_skip = total_rows - len(rows_to_update)
        
        if rows_to_skip > 0:
            print(f"⏭️  {rows_to_skip} rows will be skipped (already have metadata)")
        
        if not rows_to_update:
            print("\n✅ All rows already have metadata. No updates needed.")
            return
        
        print(f"🔄 {len(rows_to_update)} rows will be processed.\n")
        
        updated_count = 0
        skipped_count = 0
        success_count = 0
        failed_count = 0
        
        for idx, i in enumerate(rows_to_update, 1):
            row = rows[i]
            url = row.get('youtube_url', '').strip()
            
            if not url:
                skipped_count += 1
                print(f"  [{idx}/{len(rows_to_update)}] ⚠️  Skipping row {i+1} (no URL)")
                continue
                
            if not self.needs_update(row):
                skipped_count += 1
                if self.verbose:
                    print(f"  [{idx}/{len(rows_to_update)}] ⏭️  Skipping row {i+1} (already has metadata)")
                continue
            
            updated_row, success = self.update_row(row, idx, len(rows_to_update))
            rows[i] = updated_row
            updated_count += 1
            
            if success:
                success_count += 1
            else:
                failed_count += 1
            
            # Add small delay to avoid rate limiting
            if not self.offline:
                time.sleep(0.5)
        
        # Final summary
        print("\n" + "=" * 60)
        print("📈 Summary")
        print("=" * 60)
        print(f"  ✅ Successfully updated: {success_count} rows")
        if failed_count > 0:
            print(f"  ❌ Failed to fetch: {failed_count} rows")
        print(f"  ⏭️  Skipped: {skipped_count} rows")
        print(f"  📝 Total processed: {updated_count} rows")
        print("=" * 60)
        
        if updated_count > 0:
            self.write_csv(rows)
            print(f"\n💾 CSV file updated: {self.csv_path}")
        else:
            print("\n✅ No updates needed.")


def main():
    parser = argparse.ArgumentParser(
        description='Update youtube-tools/youtube.csv with YouTube video metadata',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Update only rows with missing metadata
  python update_youtube_csv.py
  
  # Force update all rows (useful for updating view counts that change over time)
  python update_youtube_csv.py --force
  
  # Force update with VPN
  python update_youtube_csv.py --force --vpn
  
  # Skip rows that already have metadata
  python update_youtube_csv.py --skip-existing
  
  # Dry run to see what would be updated
  python update_youtube_csv.py --dry-run --verbose
  
  # Use VPN proxy
  python update_youtube_csv.py --vpn
        """
    )
    parser.add_argument('--csv-path', 
                       help='Path to CSV file (default: youtube-tools/youtube.csv)',
                       type=Path)
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without making changes')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Enable verbose output')
    parser.add_argument('--offline', action='store_true', 
                       help='Run in offline mode (no network requests)')
    parser.add_argument('--proxy', 
                       help='HTTP/HTTPS proxy URL (e.g., http://127.0.0.1:1087)')
    parser.add_argument('--vpn', action='store_true',
                       help='Use VPN proxy at http://0.0.0.0:1087')
    parser.add_argument('--force', action='store_true',
                       help='Force update all rows (including those with existing metadata). Useful for updating view counts that change over time.')
    parser.add_argument('--skip-existing', action='store_true',
                       help='Skip rows that already have any metadata')
    
    args = parser.parse_args()
    
    # Determine CSV path
    if args.csv_path:
        csv_path = Path(args.csv_path)
    else:
        # Default to youtube-tools/youtube.csv (same directory as script)
        script_dir = Path(__file__).parent
        csv_path = script_dir / "youtube.csv"
    
    # Determine proxy settings (priority: --proxy > --vpn > environment variables)
    proxy = args.proxy
    if not proxy and args.vpn:
        proxy = 'http://0.0.0.0:1087'
    if not proxy:
        proxy = os.environ.get('http_proxy') or os.environ.get('https_proxy')
    
    if proxy and not args.offline:
        print(f"Using proxy: {proxy}")
    
    # Validate arguments
    if args.force and args.skip_existing:
        print("Error: --force and --skip-existing cannot be used together")
        sys.exit(1)
    
    updater = YouTubeCSVUpdater(
        csv_path=csv_path,
        dry_run=args.dry_run,
        verbose=args.verbose,
        offline=args.offline,
        proxy=proxy,
        force=args.force,
        skip_existing=args.skip_existing
    )
    
    updater.update_csv()


if __name__ == "__main__":
    main()

