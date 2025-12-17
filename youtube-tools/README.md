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

### Generate Website

```bash
# Generate HTML website for English (default: docs/overrides/videos.html)
python youtube-tools/generate_youtube_website.py

# Generate for all languages (creates videos.html, videos.zh.html, etc.)
python youtube-tools/generate_youtube_website.py --all-languages

# Generate for specific language
python youtube-tools/generate_youtube_website.py --language zh

# Specify custom output file
python youtube-tools/generate_youtube_website.py --output custom.html
```

The generated website will be accessible at `http://0.0.0.0:8002/videos` when running the MkDocs server. Language-specific versions are available at `/zh/videos`, `/ja/videos`, etc.

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


## Static i18n Generation (SEO-Optimized)

The `generate_youtube_website.py` script now generates language-specific static HTML files for SEO:

### Generated Files

- `docs/partials/videos.html` (English)
- `docs/partials/videos.zh.html` (Chinese)
- `docs/partials/videos.ja.html` (Japanese)
- `docs/partials/videos.ko.html` (Korean)
- `docs/partials/videos.fr.html` (French)
- `docs/partials/videos.de.html` (German)
- `docs/partials/videos.it.html` (Italian)
- `docs/partials/videos.es.html` (Spanish)
- `docs/partials/videos.pt.html` (Portuguese)
- `docs/partials/videos.ro.html` (Romanian)
- `docs/partials/videos-grid.html` (Shared grid, included by all language files)

### How It Works

1. Reads video data from `youtube.csv`
2. Loads translations from `docs/assets/i18n-sites/youtube-videos.json`
3. Generates static HTML with translations applied at build time
4. Each language gets its own file for perfect SEO indexing

### Workflow

```bash
# 1. Update video data or translations
vim youtube-tools/youtube.csv
vim docs/assets/i18n-sites/youtube-videos.json

# 2. Regenerate all language files
python youtube-tools/generate_youtube_website.py

# 3. Commit generated files
git add docs/partials/videos*.html
git commit -m "Update videos page"
```

### SEO Benefits

- ✅ Search engines see fully translated static HTML
- ✅ No JavaScript required for translation
- ✅ Each language URL serves its own static file
- ✅ Perfect indexing for all languages

