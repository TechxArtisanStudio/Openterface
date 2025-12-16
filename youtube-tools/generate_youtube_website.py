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
    
    # Translation dictionaries for UI strings
    TRANSLATIONS = {
        'en': {
            'title': '📺 YouTube Videos',
            'subtitle': 'Openterface Product Reviews & Updates',
            'total_videos': 'Total Videos',
            'languages': 'Languages',
            'products': 'Products',
            'views': 'views',
            'home_page': 'Home Page',
            'unknown_channel': 'Unknown Channel'
        },
        'zh': {
            'title': '📺 YouTube 视频',
            'subtitle': 'Openterface 产品评测与更新',
            'total_videos': '视频总数',
            'languages': '语言',
            'products': '产品',
            'views': '次观看',
            'home_page': '首页',
            'unknown_channel': '未知频道'
        },
        'ja': {
            'title': '📺 YouTube 動画',
            'subtitle': 'Openterface 製品レビューとアップデート',
            'total_videos': '動画総数',
            'languages': '言語',
            'products': '製品',
            'views': '回視聴',
            'home_page': 'ホームページ',
            'unknown_channel': '不明なチャンネル'
        },
        'ko': {
            'title': '📺 YouTube 동영상',
            'subtitle': 'Openterface 제품 리뷰 및 업데이트',
            'total_videos': '동영상 총수',
            'languages': '언어',
            'products': '제품',
            'views': '회 조회',
            'home_page': '홈페이지',
            'unknown_channel': '알 수 없는 채널'
        },
        'fr': {
            'title': '📺 Vidéos YouTube',
            'subtitle': 'Avis et mises à jour des produits Openterface',
            'total_videos': 'Total des vidéos',
            'languages': 'Langues',
            'products': 'Produits',
            'views': 'vues',
            'home_page': 'Page d\'accueil',
            'unknown_channel': 'Chaîne inconnue'
        },
        'de': {
            'title': '📺 YouTube Videos',
            'subtitle': 'Openterface Produktbewertungen & Updates',
            'total_videos': 'Gesamt Videos',
            'languages': 'Sprachen',
            'products': 'Produkte',
            'views': 'Aufrufe',
            'home_page': 'Startseite',
            'unknown_channel': 'Unbekannter Kanal'
        },
        'it': {
            'title': '📺 Video YouTube',
            'subtitle': 'Recensioni e aggiornamenti prodotti Openterface',
            'total_videos': 'Totale video',
            'languages': 'Lingue',
            'products': 'Prodotti',
            'views': 'visualizzazioni',
            'home_page': 'Home Page',
            'unknown_channel': 'Canale sconosciuto'
        },
        'es': {
            'title': '📺 Videos de YouTube',
            'subtitle': 'Reseñas y actualizaciones de productos Openterface',
            'total_videos': 'Total de videos',
            'languages': 'Idiomas',
            'products': 'Productos',
            'views': 'visualizaciones',
            'home_page': 'Página de inicio',
            'unknown_channel': 'Canal desconocido'
        },
        'pt': {
            'title': '📺 Vídeos do YouTube',
            'subtitle': 'Avaliações e atualizações de produtos Openterface',
            'total_videos': 'Total de vídeos',
            'languages': 'Idiomas',
            'products': 'Produtos',
            'views': 'visualizações',
            'home_page': 'Página inicial',
            'unknown_channel': 'Canal desconhecido'
        },
        'ro': {
            'title': '📺 Videoclipuri YouTube',
            'subtitle': 'Recenzii și actualizări produse Openterface',
            'total_videos': 'Total videoclipuri',
            'languages': 'Limbi',
            'products': 'Produse',
            'views': 'vizualizări',
            'home_page': 'Pagina principală',
            'unknown_channel': 'Canal necunoscut'
        }
    }
    
    SUPPORTED_LANGUAGES = ['en', 'zh', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ro']
    
    def __init__(self, csv_path: Path, output_path: Path = None, language: str = 'en'):
        self.csv_path = csv_path
        self.language = language if language in self.SUPPORTED_LANGUAGES else 'en'
        self.translations = self.TRANSLATIONS.get(self.language, self.TRANSLATIONS['en'])
        
        if output_path:
            self.output_path = output_path
        else:
            # Default to docs/partials/videos.html
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
        
        # Get translations for current language
        t = self.translations
        
        # Generate HTML partial that works within MkDocs Material theme
        # Note: CSS is now in docs/assets/stylesheets/youtube-videos.css
        html_content = f"""<!-- YouTube Videos Grid - Generated from youtube.csv (Language: {self.language}) -->

    <div class="youtube-videos-page">
    <div class="youtube-stats">
        <div class="youtube-stat-card">
            <div class="number">{len(sorted_rows)}</div>
            <div class="label">{t['total_videos']}</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{len(set(r.get('language', '').strip() for r in sorted_rows if r.get('language', '').strip()))}</div>
            <div class="label">{t['languages']}</div>
        </div>
        <div class="youtube-stat-card">
            <div class="number">{len(set(r.get('product', '').strip() for r in sorted_rows if r.get('product', '').strip()))}</div>
            <div class="label">{t['products']}</div>
        </div>
    </div>
    
    <div class="youtube-videos-grid">
"""
        
        for row in sorted_rows:
            # Render video card using template
            card_html = self.render_video_card(row)
            html_content += f"            {card_html}\n"
        
        html_content += """
    </div>
</div>
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
  # Generate website (default: docs/partials/videos.html)
  python generate_youtube_website.py
  
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
        language='en'  # Default to English, but only one file is generated
    )
    generator.generate()


if __name__ == "__main__":
    main()

