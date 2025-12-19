#!/usr/bin/env python3
"""
Home Videos Generator

This script reads youtube.csv and generates an HTML partial for the homepage
that displays the top 10 videos in a horizontal scrolling carousel.

Usage:
    python generate_home_videos.py
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List, Dict
from datetime import datetime
import html
import re


class HomeVideosGenerator:
    """Generates homepage video carousel HTML from YouTube CSV data."""
    
    def __init__(self, csv_path: Path = None):
        if csv_path:
            self.csv_path = csv_path
        else:
            script_dir = Path(__file__).parent
            self.csv_path = script_dir / "youtube.csv"
        
        script_dir = Path(__file__).parent
        docs_dir = script_dir.parent / "docs"
        partials_dir = docs_dir / "overrides" / "partials"
        partials_dir.mkdir(parents=True, exist_ok=True)
        self.output_path = partials_dir / "home-videos.html"
    
    def read_csv(self) -> List[Dict[str, str]]:
        """Read CSV file and return list of rows."""
        rows = []
        
        if not self.csv_path.exists():
            print(f"Error: CSV file not found: {self.csv_path}")
            return rows
            
        try:
            with open(self.csv_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalize keys (remove BOM if present)
                    normalized_row = {}
                    for key, value in row.items():
                        normalized_key = key.lstrip('\ufeff')
                        normalized_row[normalized_key] = value
                    
                    # Skip rows where youtube_url is empty or is the header
                    url = normalized_row.get('youtube_url', '').strip()
                    if url and url != 'youtube_url':
                        rows.append(normalized_row)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            
        return rows
    
    def extract_video_id(self, url: str) -> str:
        """Extract video ID from YouTube URL."""
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([^&\n?#]+)',
            r'youtube\.com/watch\?.*v=([^&\n?#]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return ''
    
    def format_views(self, views: str) -> str:
        """Format view count for display."""
        if not views or not views.strip():
            return "0"
        
        try:
            views_int = int(views)
            if views_int >= 1000000:
                return f"{views_int/1000000:.1f}M"
            elif views_int >= 1000:
                return f"{views_int/1000:.1f}K"
            else:
                return str(views_int)
        except (ValueError, TypeError):
            return "0"
    
    def format_date(self, date_str: str, short: bool = False) -> str:
        """Format date for display."""
        if not date_str or not date_str.strip():
            return ""
        
        # Try to parse different date formats
        date_str = date_str.strip()
        
        # Handle YYYY/MM/DD format
        if '/' in date_str:
            try:
                parts = date_str.split('/')
                if len(parts) == 3:
                    year, month, day = parts
                    formatted = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                else:
                    formatted = date_str
            except:
                formatted = date_str
        # Handle YYYY-MM-DD format
        elif '-' in date_str:
            formatted = date_str.split()[0]  # Take just the date part
        else:
            formatted = date_str
        
        # For short format (mobile), show MM/DD/YY or MM/DD
        if short and formatted:
            try:
                if '-' in formatted:
                    parts = formatted.split('-')
                    if len(parts) == 3:
                        year, month, day = parts
                        # Show MM/DD/YY format for mobile
                        return f"{month}/{day}/{year[-2:]}"
            except:
                pass
        
        return formatted
    
    def parse_date_for_sort(self, date_str: str) -> datetime:
        """Parse date string for sorting (newest first)."""
        if not date_str or not date_str.strip():
            return datetime.min
        
        date_str = date_str.strip()
        
        # Try YYYY-MM-DD format
        if '-' in date_str:
            try:
                date_part = date_str.split()[0]
                return datetime.strptime(date_part, '%Y-%m-%d')
            except:
                pass
        
        # Try YYYY/MM/DD format
        if '/' in date_str:
            try:
                parts = date_str.split('/')
                if len(parts) == 3:
                    year, month, day = parts
                    return datetime(int(year), int(month), int(day))
            except:
                pass
        
        return datetime.min
    
    def sort_videos(self, rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Sort videos by z_index (desc), views (desc), date (desc/newest first)."""
        def sort_key(row):
            # z_index (descending, default 0)
            z_index = row.get('z_index', '').strip()
            try:
                z_val = int(z_index) if z_index else 0
            except (ValueError, TypeError):
                z_val = 0
            
            # views (descending, default 0)
            views = row.get('views', '').strip()
            try:
                v_val = int(views) if views else 0
            except (ValueError, TypeError):
                v_val = 0
            
            # date (descending/newest first)
            date_str = row.get('date', '').strip()
            date_obj = self.parse_date_for_sort(date_str)
            # Use negative timestamp for descending order (newest first)
            date_val = -date_obj.timestamp() if date_obj != datetime.min else 0
            
            return (-z_val, -v_val, date_val)
        
        return sorted(rows, key=sort_key)
    
    def generate_video_item_html(self, row: Dict[str, str]) -> str:
        """Generate HTML for a single video item."""
        url = row.get('youtube_url', '').strip()
        title_raw = row.get('title', '').strip()
        author_raw = row.get('author_name', '').strip()
        channel_avatar = row.get('thumbnail_url', '').strip()
        video_thumbnail = row.get('video_thumbnail_url', '').strip()
        date = self.format_date(row.get('date', '').strip())
        views_src = row.get('views', '').strip()
        views_formatted = self.format_views(views_src)
        
        video_id = self.extract_video_id(url)
        
        # Use video_thumbnail_url for video cover, fallback to YouTube thumbnail URL
        if not video_thumbnail and video_id:
            video_thumbnail = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        elif not video_thumbnail:
            video_thumbnail = "https://via.placeholder.com/320x180?text=No+Thumbnail"
        
        # Escape for HTML attributes
        url_escaped = html.escape(url)
        title_escaped_attr = html.escape(title_raw)
        author_escaped_attr = html.escape(author_raw)
        channel_avatar_escaped = html.escape(channel_avatar)
        video_thumbnail_escaped = html.escape(video_thumbnail)
        
        # For display content, escape but convert &#x27; back to apostrophe for readability
        title_display = html.escape(title_raw).replace('&#x27;', "'")
        author_display = html.escape(author_raw).replace('&#x27;', "'") if author_raw else 'Unknown'
        
        # Build channel avatar image
        if channel_avatar:
            channel_avatar_img = f'<img src="{channel_avatar_escaped}" alt="{author_display}" class="home-video-channel-avatar" onerror="this.style.display=\'none\'">'
        else:
            channel_avatar_img = ''
        
        return f"""      <div class="home-video-item" 
           data-video-url="{url_escaped}"
           data-video-title="{title_escaped_attr}"
           data-channel-name="{author_escaped_attr}"
           data-channel-avatar="{channel_avatar_escaped}"
           data-views="{html.escape(views_src)}"
           data-date="{html.escape(date)}"
           data-thumbnail="{video_thumbnail_escaped}">
        <a href="{url_escaped}" target="_blank" rel="noopener noreferrer" class="home-video-link">
          <div class="home-video-thumbnail">
            <img src="{video_thumbnail_escaped}" alt="{title_escaped_attr}" loading="lazy" onerror="this.src='https://via.placeholder.com/320x180?text=Image+Error'">
          </div>
          <div class="home-video-card">
            <h3 class="home-video-title">{title_display}</h3>
            <div class="home-video-meta">
              <div class="home-video-channel">
                {channel_avatar_img}
                <span class="home-video-channel-name">{author_display}</span>
              </div>
            </div>
            <div class="home-video-stats">
              <span class="home-video-stat-item">👁️ {html.escape(views_formatted)}</span>
              <span class="home-video-stat-item home-video-date-wrapper">📅<span class="home-video-date">{html.escape(date) if date else 'N/A'}</span></span>
            </div>
          </div>
        </a>
      </div>
"""
    
    def generate_html(self, rows: List[Dict[str, str]]) -> str:
        """Generate HTML for homepage video carousel."""
        # Sort and take top 10
        sorted_rows = self.sort_videos(rows)
        top_10 = sorted_rows[:10]
        
        if not top_10:
            return "<!-- No videos found in CSV -->\n"
        
        html_content = """<!-- Homepage Video Carousel - Generated from youtube.csv -->
<!-- Top 10 videos sorted by z_index, views, date -->
<section class="home-videos-carousel-container">
  <div class="home-videos-carousel-wrapper">
    <div class="home-videos-carousel" id="home-videos-carousel">
"""
        
        # Generate items twice for seamless infinite scroll
        for row in top_10:
            html_content += self.generate_video_item_html(row)
        
        # Duplicate for seamless loop
        for row in top_10:
            html_content += self.generate_video_item_html(row)
        
        html_content += """    </div>
  </div>
</section>
"""
        
        return html_content
    
    def generate(self):
        """Generate the homepage videos HTML partial."""
        print("=" * 60)
        print("Homepage Videos Generator")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
        
        print(f"\n📊 Found {len(rows)} videos in CSV file.")
        
        html_content = self.generate_html(rows)
        
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ Generated: {self.output_path.name}")
            print(f"📄 Output: {self.output_path}")
        except Exception as e:
            print(f"❌ Error writing {self.output_path.name}: {e}")
            return
        
        print(f"\n✅ Generation complete!")


def main():
    parser = argparse.ArgumentParser(
        description='Generate homepage video carousel from youtube.csv',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--csv-path',
                       help='Path to CSV file (default: youtube.csv in script directory)',
                       type=Path)
    
    args = parser.parse_args()
    
    csv_path = args.csv_path if args.csv_path else None
    generator = HomeVideosGenerator(csv_path=csv_path)
    generator.generate()


if __name__ == "__main__":
    main()

