#!/usr/bin/env python3
"""
YouTube Website Generator

This script reads youtube.csv and generates an HTML website to display
YouTube video information with proper image rendering.

Usage:
    python generate_youtube_website.py [--output OUTPUT_FILE] [--template TEMPLATE_FILE]
"""

import csv
import argparse
from pathlib import Path
from typing import List, Dict
from datetime import datetime
import html


class YouTubeWebsiteGenerator:
    """Generates HTML website from YouTube CSV data."""
    
    def __init__(self, csv_path: Path, output_path: Path = None):
        self.csv_path = csv_path
        if output_path:
            self.output_path = output_path
        else:
            self.output_path = csv_path.parent / "youtube.html"
    
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
        import re
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
            return "N/A"
        
        try:
            views_int = int(views)
            if views_int >= 1000000:
                return f"{views_int/1000000:.1f}M"
            elif views_int >= 1000:
                return f"{views_int/1000:.1f}K"
            else:
                return str(views_int)
        except (ValueError, TypeError):
            return views
    
    def format_date(self, date_str: str) -> str:
        """Format date for display."""
        if not date_str or not date_str.strip():
            return "N/A"
        
        # Try to parse different date formats
        date_str = date_str.strip()
        
        # Handle YYYY/MM/DD format
        if '/' in date_str:
            try:
                parts = date_str.split('/')
                if len(parts) == 3:
                    year, month, day = parts
                    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            except:
                pass
        
        # Handle YYYY-MM-DD format
        if '-' in date_str:
            return date_str.split()[0]  # Take just the date part
        
        return date_str
    
    def get_language_name(self, code: str) -> str:
        """Get language name from code."""
        lang_names = {
            'en': 'English',
            'zh': 'Chinese',
            'ja': 'Japanese',
            'ko': 'Korean',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'es': 'Spanish',
            'pt': 'Portuguese',
            'ro': 'Romanian'
        }
        return lang_names.get(code.lower(), code.upper() if code else 'Unknown')
    
    def generate_html(self, rows: List[Dict[str, str]]) -> str:
        """Generate HTML content from CSV rows."""
        
        # Sort by z_index (descending) if available, then by views
        def sort_key(row):
            z_index = row.get('z_index', '').strip()
            views = row.get('views', '').strip()
            try:
                z_val = int(z_index) if z_index else 0
            except:
                z_val = 0
            try:
                v_val = int(views) if views else 0
            except:
                v_val = 0
            return (-z_val, -v_val)  # Negative for descending
        
        sorted_rows = sorted(rows, key=sort_key)
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Videos - Openterface</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            color: white;
            margin-bottom: 40px;
            padding: 30px 0;
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }}
        
        .stat-card .number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        
        .stat-card .label {{
            color: #666;
            margin-top: 5px;
        }}
        
        .videos-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}
        
        .video-card {{
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
        }}
        
        .video-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        }}
        
        .video-thumbnail {{
            position: relative;
            width: 100%;
            padding-top: 56.25%; /* 16:9 aspect ratio */
            background: #f0f0f0;
            overflow: hidden;
        }}
        
        .video-thumbnail img {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        .video-thumbnail .play-overlay {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 60px;
            height: 60px;
            background: rgba(255, 0, 0, 0.9);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        
        .video-card:hover .play-overlay {{
            opacity: 1;
        }}
        
        .play-overlay::after {{
            content: '';
            width: 0;
            height: 0;
            border-left: 20px solid white;
            border-top: 12px solid transparent;
            border-bottom: 12px solid transparent;
            margin-left: 4px;
        }}
        
        .video-content {{
            padding: 20px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }}
        
        .video-title {{
            font-size: 1.1em;
            font-weight: 600;
            margin-bottom: 12px;
            line-height: 1.4;
            color: #333;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .video-title a {{
            color: #333;
            text-decoration: none;
            transition: color 0.3s ease;
        }}
        
        .video-title a:hover {{
            color: #667eea;
        }}
        
        .video-meta {{
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }}
        
        .channel-info {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .channel-avatar {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            object-fit: cover;
        }}
        
        .channel-name {{
            font-size: 0.9em;
            color: #666;
            font-weight: 500;
        }}
        
        .video-stats {{
            display: flex;
            gap: 15px;
            font-size: 0.85em;
            color: #888;
            flex-wrap: wrap;
        }}
        
        .stat-item {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        
        .video-description {{
            font-size: 0.9em;
            color: #666;
            line-height: 1.5;
            margin-top: 12px;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            flex-grow: 1;
        }}
        
        .video-tags {{
            display: flex;
            gap: 8px;
            margin-top: 15px;
            flex-wrap: wrap;
        }}
        
        .tag {{
            background: #f0f0f0;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.8em;
            color: #666;
        }}
        
        .tag.language {{
            background: #e3f2fd;
            color: #1976d2;
        }}
        
        .tag.product {{
            background: #f3e5f5;
            color: #7b1fa2;
        }}
        
        .tag.type {{
            background: #fff3e0;
            color: #e65100;
        }}
        
        .tag.home-page {{
            background: #e8f5e9;
            color: #388e3c;
        }}
        
        footer {{
            text-align: center;
            color: white;
            margin-top: 50px;
            padding: 20px 0;
            opacity: 0.8;
        }}
        
        @media (max-width: 768px) {{
            .videos-grid {{
                grid-template-columns: 1fr;
            }}
            
            header h1 {{
                font-size: 2em;
            }}
            
            .stats {{
                gap: 15px;
            }}
            
            .stat-card {{
                padding: 15px 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📺 YouTube Videos</h1>
            <p>Openterface Product Reviews & Updates</p>
        </header>
        
        <div class="stats">
            <div class="stat-card">
                <div class="number">{len(sorted_rows)}</div>
                <div class="label">Total Videos</div>
            </div>
            <div class="stat-card">
                <div class="number">{len(set(r.get('language', '').strip() for r in sorted_rows if r.get('language', '').strip()))}</div>
                <div class="label">Languages</div>
            </div>
            <div class="stat-card">
                <div class="number">{len(set(r.get('product', '').strip() for r in sorted_rows if r.get('product', '').strip()))}</div>
                <div class="label">Products</div>
            </div>
        </div>
        
        <div class="videos-grid">
"""
        
        for row in sorted_rows:
            url = row.get('youtube_url', '').strip()
            title = html.escape(row.get('title', '').strip())
            author = html.escape(row.get('author_name', '').strip())
            channel_avatar = row.get('thumbnail_url', '').strip()  # Channel avatar
            video_thumbnail = row.get('video_thumbnail_url', '').strip()  # Video cover thumbnail
            date = self.format_date(row.get('date', '').strip())
            views = self.format_views(row.get('views', '').strip())
            description = html.escape(row.get('description', '').strip())
            language = row.get('language', '').strip()
            product = row.get('product', '').strip()
            video_type = row.get('type', '').strip()
            home_page = row.get('home_page', '').strip()
            
            video_id = self.extract_video_id(url)
            
            # Use video_thumbnail_url for video cover, fallback to YouTube thumbnail URL
            if not video_thumbnail and video_id:
                video_thumbnail = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
            elif not video_thumbnail:
                video_thumbnail = "https://via.placeholder.com/640x360?text=No+Thumbnail"
            
            # Build tags
            tags_html = ""
            if language:
                lang_name = self.get_language_name(language)
                tags_html += f'<span class="tag language">{lang_name}</span>'
            if product:
                tags_html += f'<span class="tag product">{html.escape(product)}</span>'
            if video_type:
                tags_html += f'<span class="tag type">{html.escape(video_type)}</span>'
            if home_page:
                tags_html += f'<span class="tag home-page">Home Page</span>'
            
            html_content += f"""
            <div class="video-card">
                <a href="{url}" target="_blank" rel="noopener noreferrer">
                    <div class="video-thumbnail">
                        <img src="{html.escape(video_thumbnail)}" alt="{title}" loading="lazy" onerror="this.src='https://via.placeholder.com/640x360?text=Image+Error'">
                        <div class="play-overlay"></div>
                    </div>
                </a>
                <div class="video-content">
                    <h3 class="video-title">
                        <a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>
                    </h3>
                    <div class="video-meta">
                        <div class="channel-info">
                            {f'<img src="{html.escape(channel_avatar)}" alt="{author}" class="channel-avatar" onerror="this.style.display=\'none\'">' if channel_avatar else ''}
                            <span class="channel-name">{author or 'Unknown Channel'}</span>
                        </div>
                    </div>
                    <div class="video-stats">
                        <span class="stat-item">👁️ {views} views</span>
                        <span class="stat-item">📅 {date}</span>
                    </div>
                    {f'<div class="video-description">{description}</div>' if description else ''}
                    {f'<div class="video-tags">{tags_html}</div>' if tags_html else ''}
                </div>
            </div>
"""
        
        html_content += """
        </div>
        
        <footer>
            <p>Generated on """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """</p>
            <p>Data from youtube.csv</p>
        </footer>
    </div>
</body>
</html>
"""
        
        return html_content
    
    def generate(self):
        """Generate the HTML website."""
        print("=" * 60)
        print("YouTube Website Generator")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
        
        print(f"\n📊 Found {len(rows)} videos in CSV file.")
        print(f"📝 Generating HTML website...")
        
        html_content = self.generate_html(rows)
        
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"✅ Website generated successfully!")
            print(f"📄 Output file: {self.output_path}")
            print(f"\n💡 Open {self.output_path} in your browser to view the website.")
            
        except Exception as e:
            print(f"❌ Error writing HTML file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate HTML website from YouTube CSV data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate website with default output (youtube.html)
  python generate_youtube_website.py
  
  # Specify custom output file
  python generate_youtube_website.py --output videos.html
        """
    )
    parser.add_argument('--csv-path',
                       help='Path to CSV file (default: youtube.csv in script directory)',
                       type=Path)
    parser.add_argument('--output', '-o',
                       help='Output HTML file (default: youtube.html)',
                       type=Path)
    
    args = parser.parse_args()
    
    # Determine CSV path
    if args.csv_path:
        csv_path = Path(args.csv_path)
    else:
        # Default to youtube.csv in script directory
        script_dir = Path(__file__).parent
        csv_path = script_dir / "youtube.csv"
    
    generator = YouTubeWebsiteGenerator(csv_path=csv_path, output_path=args.output)
    generator.generate()


if __name__ == "__main__":
    main()

