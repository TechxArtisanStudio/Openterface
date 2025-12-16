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
import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime
import html


class YouTubeWebsiteGenerator:
    """Generates HTML website from YouTube CSV data."""
    
    @staticmethod
    def load_i18n_config() -> Dict:
        """Load i18n configuration from JSON file."""
        script_dir = Path(__file__).parent
        i18n_path = script_dir / "i18n.json"
        
        if not i18n_path.exists():
            raise FileNotFoundError(
                f"i18n configuration file not found: {i18n_path}\n"
                "Please ensure i18n.json exists in the same directory as the script."
            )
        
        try:
            with open(i18n_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in i18n.json: {e}")
        except Exception as e:
            raise RuntimeError(f"Error loading i18n.json: {e}")
    
    @classmethod
    def get_translations(cls) -> Dict[str, Dict[str, str]]:
        """Get translations dictionary from i18n config."""
        config = cls.load_i18n_config()
        return config.get('translations', {})
    
    @classmethod
    def get_supported_languages(cls) -> List[str]:
        """Get supported languages list from i18n config."""
        config = cls.load_i18n_config()
        return config.get('supported_languages', ['en'])
    
    def __init__(self, csv_path: Path, output_path: Path = None, language: str = 'en'):
        self.csv_path = csv_path
        
        # Load i18n configuration
        self._i18n_config = self.load_i18n_config()
        self._translations = self._i18n_config.get('translations', {})
        self._supported_languages = self._i18n_config.get('supported_languages', ['en'])
        
        # Set language and translations
        self.language = language if language in self._supported_languages else 'en'
        self.translations = self._translations.get(self.language, self._translations.get('en', {}))
        
        if output_path:
            self.output_path = output_path
        else:
            # Default to docs/partials/videos.html (single i18n-enabled file)
            script_dir = Path(__file__).parent
            docs_dir = script_dir.parent / "docs"
            partials_dir = docs_dir / "partials"
            partials_dir.mkdir(parents=True, exist_ok=True)
            self.output_path = partials_dir / "videos.html"
    
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
    
    def load_video_card_template(self) -> str:
        """Load the video card template from youtube-tools directory."""
        script_dir = Path(__file__).parent
        template_path = script_dir / "youtube-video-card.html"
        
        if template_path.exists():
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Remove HTML comments from template
                    import re
                    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
                    return content.strip()
            except Exception as e:
                print(f"Warning: Could not load template from {template_path}: {e}")
        
        # Fallback to inline template if file doesn't exist
        return """<div class="youtube-video-card">
    <a href="{url}" target="_blank" rel="noopener noreferrer">
        <div class="youtube-video-thumbnail">
            <img src="{video_thumbnail}" alt="{title}" loading="lazy" onerror="this.src='https://via.placeholder.com/640x360?text=Image+Error'">
            <div class="play-overlay"></div>
        </div>
    </a>
    <div class="youtube-video-content">
        <h3 class="youtube-video-title">
            <a href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>
        </h3>
        <div class="youtube-video-meta">
            <div class="youtube-channel-info">
                {channel_avatar_img}
                <span class="youtube-channel-name">{channel_name}</span>
            </div>
        </div>
        <div class="youtube-video-stats">
            <span class="youtube-stat-item">👁️ {views} {views_label}</span>
            <span class="youtube-stat-item">📅 {date}</span>
        </div>
        {description_html}
        {tags_html}
    </div>
</div>"""
    
    def render_video_card(self, row: Dict[str, str]) -> str:
        """Render a single video card using the template."""
        url = row.get('youtube_url', '').strip()
        title = html.escape(row.get('title', '').strip())
        author = html.escape(row.get('author_name', '').strip())
        channel_avatar = row.get('thumbnail_url', '').strip()
        video_thumbnail = row.get('video_thumbnail_url', '').strip()
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
        
        # Build channel avatar image
        if channel_avatar:
            channel_avatar_img = f'<img src="{html.escape(channel_avatar)}" alt="{author}" class="youtube-channel-avatar" onerror="this.style.display=\'none\'">'
        else:
            channel_avatar_img = ''
        
        # Build description HTML
        if description:
            description_html = f'<div class="youtube-video-description">{description}</div>'
        else:
            description_html = ''
        
        # Build tags HTML
        tags_html = ""
        if language or product or video_type or home_page:
            tags_html = '<div class="youtube-video-tags">'
            if language:
                lang_name = self.get_language_name(language)
                tags_html += f'<span class="youtube-tag language">{lang_name}</span>'
            if product:
                tags_html += f'<span class="youtube-tag product">{html.escape(product)}</span>'
            if video_type:
                tags_html += f'<span class="youtube-tag type">{html.escape(video_type)}</span>'
            if home_page:
                tags_html += f'<span class="youtube-tag home-page">{self.translations["home_page"]}</span>'
            tags_html += '</div>'
        
        # Load template and render
        template = self.load_video_card_template()
        
        # Replace template variables
        card_html = template.format(
            url=url,
            title=title,
            video_thumbnail=html.escape(video_thumbnail),
            channel_avatar_img=channel_avatar_img,
            channel_name=author or self.translations['unknown_channel'],
            views=views,
            views_label=self.translations['views'],
            date=date,
            description_html=description_html,
            tags_html=tags_html
        )
        
        return card_html
    
    def generate_videos_grid(self, rows: List[Dict[str, str]]) -> str:
        """Generate the videos grid HTML (shared across all languages)."""
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
        
        # Generate the video grid HTML
        grid_html = """<!-- YouTube Videos Grid - Generated from youtube.csv -->
    <div class="youtube-videos-grid">
"""
        
        for row in sorted_rows:
            # Render video card using template
            card_html = self.render_video_card(row)
            grid_html += f"            {card_html}\n"
        
        grid_html += """    </div>
"""
        
        return grid_html
    
    def generate_html(self, rows: List[Dict[str, str]]) -> str:
        """Generate HTML content from CSV rows with i18n support."""
        
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
        
        # Get all translations for embedding as data attribute
        all_translations = self._translations
        
        # Convert translations to JSON string, escaping single quotes for HTML attribute
        translations_json = json.dumps(all_translations, ensure_ascii=False)
        # Escape single quotes for use in HTML attribute (but keep double quotes for JSON)
        translations_json_escaped = translations_json.replace("'", "&#39;")
        
        # Get default English translations for fallback text content
        t = self._translations.get('en', {})
        
        # Generate HTML partial with i18n support
        # Note: CSS is now in docs/assets/stylesheets/youtube-videos.css
        # The video grid is in a separate partial: videos-grid.html
        html_content = f"""<!-- YouTube Videos Page - Generated from youtube.csv (i18n-enabled) -->

    <div class="youtube-videos-page" 
         i18n-lang="auto" 
         data-translations='{translations_json_escaped}'>
    <h1 class="youtube-videos-title" data-i18n-key="title">{t.get('title', '📺 YouTube Videos')}</h1>
    <div class="youtube-stats">
        <div class="youtube-stat-card">
            <div class="number">{len(sorted_rows)}</div>
            <div class="label" data-i18n-key="total_videos">{t.get('total_videos', 'Total Videos')}</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{len(set(r.get('language', '').strip() for r in sorted_rows if r.get('language', '').strip()))}</div>
            <div class="label" data-i18n-key="languages">{t.get('languages', 'Languages')}</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{len(set(r.get('product', '').strip() for r in sorted_rows if r.get('product', '').strip()))}</div>
            <div class="label" data-i18n-key="products">{t.get('products', 'Products')}</div>
        </div>
    </div>
    
    {{% include "partials/videos-grid.html" %}}
</div>

<script>
(function() {{
    'use strict';
    
    // Get the page container
    const pageElement = document.querySelector('.youtube-videos-page');
    if (!pageElement) return;
    
    // Load translations from data attribute
    let translations = {{}};
    try {{
        const translationsJson = pageElement.getAttribute('data-translations');
        if (translationsJson) {{
            // Unescape HTML entities
            const unescaped = translationsJson.replace(/&#39;/g, "'");
            translations = JSON.parse(unescaped);
        }}
    }} catch (e) {{
        console.warn('Failed to parse translations:', e);
        return;
    }}
    
    // Detect current language from URL path
    // MkDocs static i18n uses URLs like: /zh/videos/, /es/videos/, etc.
    function detectLanguageFromURL() {{
        const path = window.location.pathname;
        const segments = path.split('/').filter(segment => segment);
        
        // Supported language codes (from i18n.json)
        const supportedLangs = {json.dumps(self._supported_languages)};
        
        // Check if first segment is a language code
        if (segments.length > 0 && supportedLangs.includes(segments[0])) {{
            return segments[0];
        }}
        
        // Default to English if no language code found
        return 'en';
    }}
    
    // Get current language
    const i18nLang = pageElement.getAttribute('i18n-lang');
    let currentLang = 'en';
    
    if (i18nLang === 'auto') {{
        currentLang = detectLanguageFromURL();
    }} else if (i18nLang && translations[i18nLang]) {{
        currentLang = i18nLang;
    }}
    
    // Get translations for current language (fallback to English)
    const t = translations[currentLang] || translations['en'] || {{}};
    
    // Update all elements with data-i18n-key attribute
    pageElement.querySelectorAll('[data-i18n-key]').forEach(element => {{
        const key = element.getAttribute('data-i18n-key');
        if (t[key]) {{
            element.textContent = t[key];
        }}
    }});
}})();
</script>
"""
        
        return html_content
    
    def generate(self, generate_all_languages: bool = False):
        """Generate the HTML website."""
        print("=" * 60)
        print("YouTube Website Generator")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
        
        print(f"\n📊 Found {len(rows)} videos in CSV file.")
        
        # First, generate the shared videos-grid.html
        print(f"📝 Generating shared videos-grid.html...")
        grid_html = self.generate_videos_grid(rows)
        
        script_dir = Path(__file__).parent
        docs_dir = script_dir.parent / "docs"
        partials_dir = docs_dir / "partials"
        grid_path = partials_dir / "videos-grid.html"
        
        try:
            with open(grid_path, 'w', encoding='utf-8') as f:
                f.write(grid_html)
            print(f"  ✅ Generated: {grid_path.name}")
        except Exception as e:
            print(f"  ❌ Error writing {grid_path.name}: {e}")
            return
        
        # Generate single i18n-enabled videos.html (works for all languages)
        print(f"📝 Generating i18n-enabled videos.html...")
        html_content = self.generate_html(rows)
        
        videos_path = partials_dir / "videos.html"
        try:
            with open(videos_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"  ✅ Generated: {videos_path.name} (i18n-enabled for all languages)")
        except Exception as e:
            print(f"  ❌ Error writing {videos_path.name}: {e}")
            return
        
        if generate_all_languages:
            # Legacy mode: This now just generates the single file
            print(f"\n✅ Generation complete!")
            print(f"📄 Files:")
            print(f"   - {grid_path.name} (shared grid)")
            print(f"   - {videos_path.name} (single i18n-enabled file for all languages)")
        else:
            # Single file generation (already done above)
            print(f"\n✅ Generation complete!")
            print(f"📄 Files:")
            print(f"   - {grid_path.name} (shared grid)")
            print(f"   - {videos_path.name} (i18n-enabled for all languages)")
            print(f"\n💡 The videos.html file automatically detects language from URL path.")


def main():
    parser = argparse.ArgumentParser(
        description='Generate HTML website from YouTube CSV data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate website for English (default: docs/partials/videos.html)
  python generate_youtube_website.py
  
  # Generate for all languages
  python generate_youtube_website.py --all-languages
  
  # Generate for specific language
  python generate_youtube_website.py --language zh
  
  # Specify custom output file
  python generate_youtube_website.py --output custom.html
        """
    )
    parser.add_argument('--csv-path',
                       help='Path to CSV file (default: youtube.csv in script directory)',
                       type=Path)
    parser.add_argument('--output', '-o',
                       help='Output HTML file (default: docs/partials/videos.html)',
                       type=Path)
    parser.add_argument('--language', '-l',
                       help='Language code (en, zh, ja, ko, fr, de, it, es, pt, ro). Default: en',
                       default='en')
    parser.add_argument('--all-languages', '-a', action='store_true',
                       help='Generate HTML files for all supported languages')
    
    args = parser.parse_args()
    
    # Determine CSV path
    if args.csv_path:
        csv_path = Path(args.csv_path)
    else:
        # Default to youtube.csv in script directory
        script_dir = Path(__file__).parent
        csv_path = script_dir / "youtube.csv"
    
    generator = YouTubeWebsiteGenerator(
        csv_path=csv_path,
        output_path=args.output,
        language=args.language
    )
    generator.generate(generate_all_languages=args.all_languages)


if __name__ == "__main__":
    main()

