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


def main():
    print("="*60)
    print("Generating All i18n Static Content")
    print("="*60)
    
    try:
        # 1. Generate hreflang partial (used by all pages)
        print("\n1️⃣  Generating hreflang partial...")
        generator = StaticPageGenerator()
        generator.generate_hreflang_partial()
        
        # 2. Generate home pages
        print("\n2️⃣  Generating home pages...")
        generator.generate_all()
        
        # 3. Generate videos pages
        print("\n3️⃣  Generating videos pages...")
        csv_path = script_dir.parent / "youtube-tools" / "youtube.csv"
        video_gen = YouTubeWebsiteGenerator(csv_path)  # Pass Path object, not string
        video_gen.generate()
        
        print("\n" + "="*60)
        print("✅ All i18n content generated successfully!")
        print("="*60)
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

