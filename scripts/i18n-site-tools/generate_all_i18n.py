#!/usr/bin/env python3
"""
Convenience script to generate all i18n static content.
Ensures hreflang is generated before other pages.
"""

import sys
from pathlib import Path

# Add paths
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
sys.path.insert(0, str(script_dir.parent / "youtube-tools"))

from generate_static_pages import StaticPageGenerator
from generate_youtube_website import YouTubeWebsiteGenerator
from generate_home_videos import HomeVideosGenerator


def main():
    print("="*60)
    print("Generating All i18n Static Content")
    print("="*60)
    
    try:
        script_dir = Path(__file__).parent
        
        # 1. Generate hreflang partial (used by all pages)
        print("\n1️⃣  Generating hreflang partial...")
        generator = StaticPageGenerator()
        generator.generate_hreflang_partial()
        
        # 2. Generate videos data partials from CSV (videos-grid.html)
        print("\n2️⃣  Generating videos content from CSV...")
        csv_path = script_dir.parent / "youtube-tools" / "youtube.csv"
        video_gen = YouTubeWebsiteGenerator(csv_path)
        video_gen.generate_for_i18n_pipeline()  # NEW: Use unified workflow
        
        # 2.5. Generate home videos partial (home-videos.html)
        print("\n2️⃣.5️⃣  Generating home videos carousel...")
        home_videos_gen = HomeVideosGenerator(csv_path=csv_path)
        home_videos_gen.generate()
        
        # 3. Generate static pages with translations (home + videos)
        print("\n3️⃣  Generating static pages with translations (home + videos)...")
        generator.generate_all()
        
        print("\n" + "="*60)
        print("✅ All i18n content generated successfully!")
        print("="*60)
        print("\n📊 Summary:")
        print("   • hreflang.html - Generated")
        print("   • videos-grid.html - Generated from CSV")
        print("   • home-videos.html - Generated from CSV")
        print("   • home.*.html - Generated (10 languages)")
        print("   • videos.*.html - Generated (10 languages)")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

