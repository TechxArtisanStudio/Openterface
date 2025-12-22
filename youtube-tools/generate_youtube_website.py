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
import sys
from pathlib import Path
from typing import List, Dict
from datetime import datetime
import html

# Add i18n-site-tools to path for importing I18nConfig
sys.path.insert(0, str(Path(__file__).parent.parent / "i18n-site-tools"))
from i18n_config import I18nConfig


class YouTubeWebsiteGenerator:
    """Generates HTML website from YouTube CSV data."""
    
    @staticmethod
    def load_i18n_config() -> Dict:
        """Load i18n configuration from JSON file."""
        script_dir = Path(__file__).parent
        i18n_path = script_dir.parent / "docs" / "assets" / "i18n-sites" / "videos.json"
        
        if not i18n_path.exists():
            raise FileNotFoundError(
                f"i18n configuration file not found: {i18n_path}\n"
                "Please ensure videos.json exists in the docs/assets/i18n-sites directory."
            )
        
        try:
            with open(i18n_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in videos.json: {e}")
        except Exception as e:
            raise RuntimeError(f"Error loading videos.json: {e}")
    
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
        
        # Load centralized i18n config first
        self.i18n_config = I18nConfig()
        
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
        return """<div class="youtube-video-card" data-views="{views_raw}">
    <a href="{url}" target="_blank" rel="noopener noreferrer">
        <div class="youtube-video-thumbnail">
            <img src="{video_thumbnail}" alt="{title}" class="skip-lightbox" loading="lazy" onerror="this.src='https://via.placeholder.com/640x360?text=Image+Error'">
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
        date_iso = date if date and date != "N/A" else ""
        views_src = row.get('views', '').strip()
        try:
            views_raw_int = int(views_src) if views_src else 0
        except (ValueError, TypeError):
            views_raw_int = 0
        views = self.format_views(views_src)
        description = html.escape(row.get('description', '').strip())
        language = row.get('language', '').strip()
        language_name = self.get_language_name(language) if language else ""
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
            views_raw=str(views_raw_int),
            views_label=self.translations['views'],
            date=date,
            date_iso=html.escape(date_iso),
            language=html.escape(language),
            language_name=html.escape(language_name),
            product=html.escape(product),
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
    
    def generate_html(self, rows: List[Dict[str, str]], language: str = 'en') -> str:
        """Generate HTML for a specific language (static, SEO-friendly)."""
        
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
        
        # Get translations for this language (fallback to English)
        t = self._translations.get(language, self._translations.get('en', {}))
        
        # Calculate stats from CSV data
        num_videos = len(sorted_rows)
        num_languages = len(set(r.get('language', '').strip() for r in sorted_rows if r.get('language', '').strip()))
        num_products = len(set(r.get('product', '').strip() for r in sorted_rows if r.get('product', '').strip()))
        
        # Calculate stats from CSV data
        num_videos = len(sorted_rows)
        num_languages = len(set(r.get('language', '').strip() for r in sorted_rows if r.get('language', '').strip()))
        num_products = len(set(r.get('product', '').strip() for r in sorted_rows if r.get('product', '').strip()))
        
        # Generate static HTML with translations applied (no client-side JavaScript needed)
        # Note: CSS is in docs/assets/stylesheets/youtube-videos.css
        # The video grid is in a separate partial: videos-grid.html
        html_content = f"""<!-- YouTube Videos Page - Static {language.upper()} - Generated from youtube.csv -->


<div class="youtube-videos-page">
    <h1 class="youtube-videos-title">{t.get('title', '📺 YouTube Videos')}</h1>
    <div class="youtube-stats">
        <div class="youtube-stat-card">
            <div class="number">{num_videos}</div>
            <div class="label">{t.get('total_videos', 'Total Videos')}</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{num_languages}</div>
            <div class="label">{t.get('languages', 'Languages')}</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{num_products}</div>
            <div class="label">{t.get('products', 'Products')}</div>
        </div>
    </div>
    
    {{% include "partials/videos-grid.html" %}}
</div>
"""
        
        return html_content
    
    def generate_base_template(self, rows: List[Dict[str, str]]) -> str:
        """
        Generate videos-base.html as a content fragment (not a full page template).
        This will be included by markdown files via {% include "partials/videos.html" %}
        """
        # Calculate stats from CSV data
        num_videos = len(rows)
        num_languages = len(set(r.get('language', '').strip() for r in rows if r.get('language', '').strip()))
        num_products = len(set(r.get('product', '').strip() for r in rows if r.get('product', '').strip()))
        
        # Generate content fragment with data-i18n-key attributes
        # This will be processed by generate_static_pages.py to create language-specific versions
        html_content = f"""<!-- YouTube Videos Page - Generated from youtube.csv -->
<!-- This is a content fragment to be included by markdown files -->

<div class="youtube-videos-page" data-i18n-file="videos">
    <h1 class="youtube-videos-title" data-i18n-key="title">📺 YouTube Videos</h1>
    
    <div class="youtube-stats">
        <div class="youtube-stat-card">
            <div class="number">{num_videos}</div>
            <div class="label" data-i18n-key="total_videos">Total Videos</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{num_languages}</div>
            <div class="label" data-i18n-key="languages">Languages</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{num_products}</div>
            <div class="label" data-i18n-key="products">Products</div>
        </div>
    </div>

    <div class="youtube-controls" role="region" aria-label="Video controls">
        <div class="youtube-controls-row">
            <div class="youtube-control">
                <label for="yt-sort" data-i18n-key="sort_by">Sort</label>
                <select id="yt-sort" class="youtube-select">
                    <option value="newest" data-i18n-key="sort_newest">Newest first</option>
                    <option value="oldest" data-i18n-key="sort_oldest">Oldest first</option>
                </select>
            </div>

            <div class="youtube-control">
                <label for="yt-filter-product" data-i18n-key="filter_product">Product</label>
                <select id="yt-filter-product" class="youtube-select">
                    <option value="" data-i18n-key="all_products">All products</option>
                </select>
            </div>

            <div class="youtube-control">
                <label for="yt-filter-language" data-i18n-key="filter_language">Language</label>
                <select id="yt-filter-language" class="youtube-select">
                    <option value="" data-i18n-key="all_languages">All languages</option>
                </select>
            </div>

            <button type="button" class="youtube-button" id="yt-reset" data-i18n-key="reset_filters">Reset</button>
        </div>

        <div class="youtube-controls-footer" aria-live="polite">
            <span data-i18n-key="showing">Showing</span>
            <strong><span id="yt-results-visible">0</span></strong>
            /
            <span id="yt-results-total">0</span>
        </div>
    </div>
    
    {{% include "partials/videos-grid.html" %}}
</div>
"""
        
        return html_content
    
    def validate_and_get_languages(self) -> List[str]:
        """Validate JSON languages and return available languages."""
        json_languages = self._supported_languages
        
        # Validate against YAML config
        self.i18n_config.validate_json_languages(json_languages, "videos.json")
        
        # Use intersection of YAML and JSON languages
        yaml_languages = set(self.i18n_config.languages)
        available_languages = list(set(json_languages) & yaml_languages)
        
        if not available_languages:
            raise ValueError(
                "No common languages between i18n.yml and youtube-videos.json"
            )
        
        # Sort for consistent order
        available_languages.sort()
        return available_languages
    
    def generate(self, generate_all_languages: bool = False):
        """Generate static HTML files for all languages (SEO-friendly)."""
        print("=" * 60)
        print("YouTube Website Generator (Static i18n)")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
        
        print(f"\n📊 Found {len(rows)} videos in CSV file.")
        
        # First, generate the shared videos-grid.html
        print(f"\n📝 Generating shared videos-grid.html...")
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
        
        # Get validated language list
        languages_to_generate = self.validate_and_get_languages()
        
        # Generate language-specific videos.{lang}.html files (static, SEO-friendly)
        print(f"\n📝 Generating static language-specific files...")
        print(f"📊 Languages: {', '.join(languages_to_generate)}\n")
        
        for lang in languages_to_generate:
            html_content = self.generate_html(rows, language=lang)
            
            # English gets videos.html, others get videos.{lang}.html
            suffix = '' if lang == 'en' else f'.{lang}'
            output_filename = f"videos{suffix}.html"
            output_path = partials_dir / output_filename
            
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                print(f"  ✅ Generated: {output_filename} ({lang})")
            except Exception as e:
                print(f"❌ Error writing {output_filename}: {e}")
                continue
        
        print(f"\n✅ Generation complete!")
        print(f"📄 Output directory: {partials_dir}")
        print(f"\n💡 Each language now has its own static HTML file for perfect SEO.")
    
    def generate_for_i18n_pipeline(self):
        """
        New workflow: Generate data partials for the i18n pipeline.
        This keeps layout/styling decoupled from youtube.csv updates.
        """
        print("=" * 60)
        print("YouTube Content Generator (for i18n pipeline)")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
        
        print(f"\n📊 Found {len(rows)} videos in CSV file.")
        
        script_dir = Path(__file__).parent
        
        # Step 1: Generate videos-grid.html (pure data, no i18n needed)
        print(f"\n📝 Step 1: Generating videos-grid.html (video data)...")
        grid_html = self.generate_videos_grid(rows)
        
        docs_dir = script_dir.parent / "docs"
        # Output to docs/partials for MkDocs-Macros compatibility
        # (videos.*.html templates include this via {% include "videos-grid.html" %})
        partials_dir = docs_dir / "partials"
        partials_dir.mkdir(parents=True, exist_ok=True)
        
        grid_path = partials_dir / "videos-grid.html"
        
        try:
            with open(grid_path, 'w', encoding='utf-8') as f:
                f.write(grid_html)
            print(f"  ✅ Generated: {grid_path.name}")
        except Exception as e:
            print(f"  ❌ Error writing {grid_path.name}: {e}")
            return
        
        print(f"\n✅ Content generation complete!")
        print(f"\n💡 Next step:")
        print(f"   Run: python i18n-site-tools/generate_static_pages.py --template videos")
        print(f"   Or: python i18n-site-tools/generate_all_i18n.py")


def main():
    parser = argparse.ArgumentParser(
        description='Generate YouTube videos content',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # New unified workflow (recommended):
  python generate_youtube_website.py --base-template
  # Then run: python ../i18n-site-tools/generate_static_pages.py --template videos
  
  # Or use the all-in-one script:
  python ../i18n-site-tools/generate_all_i18n.py
  
  # Legacy workflow (direct generation):
  python generate_youtube_website.py --all-languages
        """
    )
    parser.add_argument('--csv-path',
                       help='Path to CSV file (default: youtube.csv in script directory)',
                       type=Path)
    parser.add_argument('--base-template', '-b',
                       action='store_true',
                       help='Generate data partials (videos-grid.html) for i18n pipeline (recommended)')
    parser.add_argument('--all-languages', '-a',
                       action='store_true',
                       help='Legacy: Generate HTML files for all languages directly')
    parser.add_argument('--output', '-o',
                       help='Legacy: Output HTML file path',
                       type=Path)
    parser.add_argument('--language', '-l',
                       help='Legacy: Language code (en, zh, ja, etc)',
                       default='en')
    
    args = parser.parse_args()
    
    # Determine CSV path
    if args.csv_path:
        csv_path = Path(args.csv_path)
    else:
        script_dir = Path(__file__).parent
        csv_path = script_dir / "youtube.csv"
    
    generator = YouTubeWebsiteGenerator(
        csv_path=csv_path,
        output_path=args.output,
        language=args.language
    )
    
    # New unified workflow (default)
    if args.base_template or (not args.all_languages and not args.output):
        generator.generate_for_i18n_pipeline()
    else:
        # Legacy direct generation
        generator.generate(generate_all_languages=args.all_languages)


if __name__ == "__main__":
    main()

