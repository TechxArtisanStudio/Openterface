# YouTube Tools

This directory contains tools for managing YouTube video metadata and language detection.

## Files

- `youtube.csv` - Main CSV file containing YouTube video metadata
- `update_youtube_csv.py` - Script to fetch and update YouTube video metadata
- `detect_youtube_language.py` - Script to detect video languages using local LLM
- `generate_youtube_website.py` - Script to generate HTML website from CSV data

## Usage

### Update YouTube Metadata

```bash
# Update only rows with missing metadata
python youtube-tools/update_youtube_csv.py

# Force update all rows (useful for updating view counts)
python youtube-tools/update_youtube_csv.py --force

# Use VPN proxy
python youtube-tools/update_youtube_csv.py --vpn

# Force update with VPN
python youtube-tools/update_youtube_csv.py --force --vpn
```

### Detect Video Languages

```bash
# Detect language for rows with empty language field
python youtube-tools/detect_youtube_language.py

# Interactive mode for failed detections
python youtube-tools/detect_youtube_language.py --interactive

# Force detect all languages
python youtube-tools/detect_youtube_language.py --force
```

### Generate Videos Page

```bash
# 1) Generate the shared grid partial from youtube.csv (recommended)
python youtube-tools/generate_youtube_website.py --base-template

# 2) Generate SEO-friendly per-language videos partials from videos-base.html + videos.json
python i18n-site-tools/generate_static_pages.py --template videos

# Or run the orchestrator (hreflang + videos-grid + all static pages)
python i18n-site-tools/generate_all_i18n.py
```

The videos page will be accessible at `/videos/` when running the MkDocs server. Language-specific versions are available at `/zh/videos/`, `/ja/videos/`, etc.

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

- Page layout + i18n keys: `i18n-site-tools/templates/videos-base.html`
- Styling: `docs/assets/stylesheets/youtube-videos.css`
- Client-side controls (sort/filter): `docs/assets/javascripts/youtube-videos-controls.js`
- Card markup (optional): `youtube-tools/youtube-video-card.html` (requires regenerating `videos-grid.html`)

### Workflow

```bash
# 1) Update YouTube data
python youtube-tools/update_youtube_csv.py

# 2) Regenerate the shared grid from youtube.csv
python youtube-tools/generate_youtube_website.py --base-template

# 3) Apply build-time i18n translations (SEO)
python i18n-site-tools/generate_static_pages.py --template videos

# (or run all-i18n orchestrator)
python i18n-site-tools/generate_all_i18n.py
```

### Why this is better

- Updating `youtube.csv` no longer overwrites your layout template.
- Redesigning the page mostly touches `videos-base.html` + CSS/JS.
- Sort/filter reads stable `data-*` attributes on cards, so it’s resilient to markup tweaks.

