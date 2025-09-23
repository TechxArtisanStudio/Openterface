#!/usr/bin/env python3
"""
YouTube Reviews Generator

This script scans the docs/product/ directory for .youtube.list files and generates
corresponding youtube.md files with enhanced metadata including video dates and view counts.

Usage:
    python generate_youtube_reviews.py [--dry-run] [--verbose] [--offline]
"""

import os
import re
import sys
import json
import time
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from urllib.parse import urlparse, parse_qs
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
        self.fallback_metadata = {}
        
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
            # Use fallback metadata if available
            fallback = self.fallback_metadata.get(video_id, {})
            empty_metadata = {
                'title': fallback.get('title', 'Video Title'),
                'author_name': fallback.get('author_name', 'Channel Name'),
                'thumbnail_url': fallback.get('thumbnail_url', ''),
                'date': fallback.get('date', ''),
                'views': fallback.get('views', ''),
                'description': fallback.get('description', '')
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
            
        # Return fallback metadata if fetch fails
        fallback = self.fallback_metadata.get(video_id, {})
        empty_metadata = {
            'title': fallback.get('title', 'Video Title'),
            'author_name': fallback.get('author_name', 'Channel Name'),
            'thumbnail_url': fallback.get('thumbnail_url', ''),
            'date': fallback.get('date', ''),
            'views': fallback.get('views', ''),
            'description': fallback.get('description', '')
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
                
                # Extract views using regex
                views_match = re.search(r'"viewCount":"(\d+)"', content)
                if views_match:
                    views = int(views_match.group(1))
                    if views >= 1000000:
                        metadata['views'] = f"{views/1000000:.1f}M"
                    elif views >= 1000:
                        metadata['views'] = f"{views/1000:.1f}K"
                    else:
                        metadata['views'] = str(views)
                
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
                        metadata['date'] = date_obj.strftime('%b %d, %Y')
                    except ValueError:
                        metadata['date'] = date_str
                
                # Extract channel avatar/icon instead of video thumbnail
                avatar_match = re.search(r'"channelThumbnail":\s*\{\s*"thumbnails":\s*\[.*?"url":\s*"([^"]+)"', content, re.DOTALL)
                if avatar_match:
                    metadata['thumbnail_url'] = avatar_match.group(1)
                        
        except Exception as e:
            # Silently fail for additional metadata
            pass

class YouTubeReviewsGenerator:
    """Generates YouTube review pages from .youtube.list files."""
    
    def __init__(self, base_dir: str = None, dry_run: bool = False, verbose: bool = False, offline: bool = False, proxy: str = None):
        self.base_dir = Path(base_dir) if base_dir else Path(__file__).parent.parent / "docs" / "product"
        self.dry_run = dry_run
        self.verbose = verbose
        self.offline = offline
        self.metadata_fetcher = YouTubeMetadataFetcher(offline_mode=offline, proxy=proxy)
        
    def parse_existing_youtube_md(self, youtube_md_path: Path) -> Dict[str, Dict[str, str]]:
        """Parse existing YouTube.md file to extract metadata for fallback."""
        metadata = {}
        
        if not youtube_md_path.exists():
            return metadata
            
        try:
            with open(youtube_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse existing format: - <a href="..."><img src="..." ...></a> **Channel**: [Title](url)
            pattern = r'- <a href="([^"]+)"><img src="([^"]*)"[^>]*></a> \*\*([^*]+)\*\*: \[([^\]]+)\]\(([^)]+)\)(?:\s*\|\s*([^|\n]+))?'
            
            if self.verbose:
                print(f"  Parsing existing content with {len(content)} characters")
            
            for match in re.finditer(pattern, content, re.MULTILINE):
                channel_url = match.group(1)
                thumbnail_url = match.group(2)
                channel_name = match.group(3)
                video_title = match.group(4)
                video_url = match.group(5)
                language = match.group(6).strip() if match.group(6) else "English"
                
                video_id = self.metadata_fetcher.extract_video_id(video_url)
                if video_id:
                    metadata[video_id] = {
                        'title': video_title,
                        'author_name': channel_name,
                        'thumbnail_url': thumbnail_url,
                        'date': '',
                        'views': '',
                        'description': ''
                    }
                    if self.verbose:
                        print(f"    Extracted metadata for {video_id}: {channel_name} - {video_title}")
                    
        except Exception as e:
            if self.verbose:
                print(f"Warning: Could not parse existing {youtube_md_path}: {e}")
                
        return metadata
        
    def find_youtube_list_files(self) -> List[Tuple[Path, Path]]:
        """Find all .youtube.list files and their corresponding youtube.md paths."""
        youtube_files = []
        
        for product_dir in self.base_dir.iterdir():
            if not product_dir.is_dir():
                continue
                
            reviews_dir = product_dir / "reviews"
            if not reviews_dir.exists():
                continue
                
            youtube_list_file = reviews_dir / ".youtube.list"
            youtube_md_file = reviews_dir / "youtube.md"
            
            if youtube_list_file.exists():
                youtube_files.append((youtube_list_file, youtube_md_file))
                if self.verbose:
                    print(f"Found .youtube.list in {product_dir.name}")
                    
        return youtube_files
    
    def read_youtube_list(self, file_path: Path) -> List[str]:
        """Read URLs from .youtube.list file."""
        urls = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        urls.append(line)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        return urls
    
    def format_views(self, views: str) -> str:
        """Format view count for display."""
        if not views:
            return ""
        return f" ({views} views)"
    
    def format_date(self, date: str) -> str:
        """Format date for display."""
        if not date:
            return ""
        return f" - {date}"
    
    
    def generate_youtube_md(self, urls: List[str], output_path: Path) -> str:
        """Generate YouTube.md content from list of URLs."""
        content = ["# YouTube", ""]
        
        for i, url in enumerate(urls):
            if self.verbose:
                print(f"Processing video {i+1}/{len(urls)}: {url}")
            
            video_id = self.metadata_fetcher.extract_video_id(url)
            if not video_id:
                print(f"Warning: Could not extract video ID from {url}")
                continue
            
            # Fetch metadata
            metadata = self.metadata_fetcher.fetch_video_metadata(video_id)
            
            # Format the entry
            channel_name = metadata.get('author_name', 'Unknown Channel')
            video_title = metadata.get('title', 'Unknown Title')
            thumbnail_url = metadata.get('thumbnail_url', '')
            date = metadata.get('date', '')
            views = metadata.get('views', '')
            
            # Create channel URL
            channel_url = f"https://www.youtube.com/@{channel_name}" if channel_name else url
            
            # Format the line
            date_str = self.format_date(date)
            views_str = self.format_views(views)
            
            line = f"- <a href=\"{channel_url}\"><img src=\"{thumbnail_url}\" alt=\"\" width=\"28\" style=\"border-radius: 50%; vertical-align: middle;\" onerror=\"this.style.display='none'\"></a> **{channel_name}**: [{video_title}]({url}){date_str}{views_str}"
            
            content.append(line)
            
            # Add small delay to avoid rate limiting
            time.sleep(0.5)
        
        return "\n".join(content)
    
    def generate_all_reviews(self):
        """Generate all YouTube review files."""
        youtube_files = self.find_youtube_list_files()
        
        if not youtube_files:
            print("No .youtube.list files found in product directories.")
            return
        
        print(f"Found {len(youtube_files)} .youtube.list files to process.")
        
        for youtube_list_path, youtube_md_path in youtube_files:
            product_name = youtube_list_path.parent.parent.name
            print(f"\nProcessing {product_name}...")
            
            # Load existing metadata for fallback
            existing_metadata = self.parse_existing_youtube_md(youtube_md_path)
            self.metadata_fetcher.fallback_metadata.update(existing_metadata)
            
            urls = self.read_youtube_list(youtube_list_path)
            if not urls:
                print(f"  No URLs found in {youtube_list_path}")
                continue
            
            print(f"  Found {len(urls)} videos")
            if existing_metadata:
                print(f"  Loaded {len(existing_metadata)} existing metadata entries")
            
            if self.dry_run:
                print(f"  [DRY RUN] Would generate {youtube_md_path}")
                continue
            
            try:
                content = self.generate_youtube_md(urls, youtube_md_path)
                
                # Create directory if it doesn't exist
                youtube_md_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Write the file
                with open(youtube_md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  Generated {youtube_md_path}")
                
            except Exception as e:
                print(f"  Error generating {youtube_md_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate YouTube review pages from .youtube.list files')
    parser.add_argument('--base-dir', help='Base directory containing product folders (default: docs/product)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--offline', action='store_true', help='Run in offline mode using existing metadata only')
    parser.add_argument('--proxy', help='HTTP/HTTPS proxy URL (e.g., http://127.0.0.1:1087)')
    
    args = parser.parse_args()
    
    # Check for proxy in environment variables if not provided as argument
    proxy = args.proxy
    if not proxy:
        proxy = os.environ.get('http_proxy') or os.environ.get('https_proxy')
    
    if proxy and not args.offline:
        print(f"Using proxy: {proxy}")
    
    generator = YouTubeReviewsGenerator(
        base_dir=args.base_dir,
        dry_run=args.dry_run,
        verbose=args.verbose,
        offline=args.offline,
        proxy=proxy
    )
    
    generator.generate_all_reviews()

if __name__ == "__main__":
    main()
