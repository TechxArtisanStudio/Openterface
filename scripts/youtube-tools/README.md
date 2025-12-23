# YouTube Tools

This directory contains tools for managing YouTube video metadata and language detection.

## Files

- `youtube.csv` - Main CSV file containing YouTube video metadata
- `update_youtube_csv.py` - Script to fetch and update YouTube video metadata
- `detect_youtube_language.py` - Script to detect video languages using local LLM
- `generate_youtube_website.py` - Script to generate HTML website from CSV data
- `generate_home_videos.py` - Script to generate homepage video carousel partial

## Usage

### Update YouTube Metadata

```bash
# Update only rows with missing metadata
python scripts/youtube-tools/update_youtube_csv.py

# Force update all rows (useful for updating view counts)
python scripts/youtube-tools/update_youtube_csv.py --force

# Use VPN proxy
python scripts/youtube-tools/update_youtube_csv.py --vpn

# Force update with VPN
python scripts/youtube-tools/update_youtube_csv.py --force --vpn
```

### Detect Video Languages

```bash
# Detect language for rows with empty language field
python scripts/youtube-tools/detect_youtube_language.py

# Interactive mode for failed detections
python scripts/youtube-tools/detect_youtube_language.py --interactive

# Force detect all languages
python scripts/youtube-tools/detect_youtube_language.py --force
```

### Generate Videos Page

```bash
# 1) Generate the shared grid partial from youtube.csv (recommended)
python scripts/youtube-tools/generate_youtube_website.py --base-template

# 2) Generate SEO-friendly per-language videos partials from videos-base.html + videos.json
python scripts/i18n-site-tools/generate_static_pages.py --template videos

# Or run the orchestrator (hreflang + videos-grid + all static pages)
python scripts/i18n-site-tools/generate_all_i18n.py
```

The videos page will be accessible at `/videos/` when running the MkDocs server. Language-specific versions are available at `/zh/videos/`, `/ja/videos/`, etc.

### Generate Homepage Video Carousel

```bash
# Generate homepage video carousel (top 10 videos)
python scripts/youtube-tools/generate_home_videos.py
```

This generates `docs/overrides/partials/home-videos.html` which displays the top 10 videos sorted by z_index (highest), views (most), and date (newest) in a horizontal auto-scrolling carousel on the homepage. The carousel shows video thumbnails by default and expands to show full video cards on hover.

**Note**: Run this script after updating `youtube.csv` to refresh the homepage carousel.

## CSV Structure

The `youtube.csv` file contains the following columns:

- `youtube_url` - YouTube video URL
- `title` - Video title
- `author_name` - Channel name
- `thumbnail_url` - Channel avatar URL
- `date` - Publication date (YYYY-MM-DD)
- `views` - View count (as number)
- `description` - Video description
- `fetch_date` - When metadata was last fetched
- `z_index` - Priority/ordering value
- `language` - Language code (en, zh, ja, ko, fr, de, it, es, pt, ro)
- `product` - Product name (e.g., minikvm, kvm-go)
- `type` - Video type (e.g., review, update)
- `home_page` - Whether to show on home page

## Notes

- The scripts automatically create backups (`.csv.backup`) before writing
- All columns are preserved when updating metadata
- Manual edits to the CSV are preserved (unless using `--force`)


## Static i18n Generation (SEO-Optimized, Decoupled)

The Videos page is built with a **decoupled pipeline**:

- **Data updates** (from `youtube.csv`) regenerate only a shared **data partial**: `docs/partials/videos-grid.html`
- **Layout/styling/controls** are hand-maintained in templates/CSS/JS
- **Translations** are applied at build-time from `docs/assets/i18n-sites/videos.json` to produce `docs/partials/videos.<lang>.html`

### Generated Files

- `docs/partials/videos-grid.html` (shared card grid generated from `youtube.csv`)
- `docs/partials/videos.html` (English, build-time translated)
- `docs/partials/videos.<lang>.html` (de/es/fr/it/ja/ko/pt/ro/zh)

### Safe files to edit for UI/design changes

- Page layout + i18n keys: `scripts/i18n-site-tools/templates/videos-base.html`
- Styling: `docs/assets/stylesheets/youtube-videos.css`
- Client-side controls (sort/filter): `docs/assets/javascripts/youtube-videos-controls.js`
- Card markup (optional): `scripts/youtube-tools/youtube-video-card.html` (requires regenerating `videos-grid.html`)

### Workflow

```bash
# 1) Update YouTube data
python scripts/youtube-tools/update_youtube_csv.py

# 2) Regenerate the shared grid from youtube.csv
python scripts/youtube-tools/generate_youtube_website.py --base-template

# 3) Apply build-time i18n translations (SEO)
python scripts/i18n-site-tools/generate_static_pages.py --template videos

# (or run all-i18n orchestrator)
python scripts/i18n-site-tools/generate_all_i18n.py
```

### Shareable URL filters (client-side)

The Videos page supports URL query params for sharing a pre-filtered/sorted view:

- `p`: product (example: `minikvm`, `kvm-go`)
- `l`: language code (example: `en`, `ja`, `fr`)
- `s`: sort (`newest`, `oldest`, or `views`)

Examples:

- `/videos/?p=minikvm&l=en&s=oldest`
- `/zh/videos/?p=kvm-go&l=fr&s=newest`

### Why this is better

- Updating `youtube.csv` no longer overwrites your layout template.
- Redesigning the page mostly touches `videos-base.html` + CSS/JS.
- Sort/filter reads stable `data-*` attributes on cards, so it’s resilient to markup tweaks.

