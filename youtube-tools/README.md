# YouTube Tools

This directory contains tools for managing YouTube video metadata and language detection.

## Files

- `youtube.csv` - Main CSV file containing YouTube video metadata
- `update_youtube_csv.py` - Script to fetch and update YouTube video metadata
- `detect_youtube_language.py` - Script to detect video languages using local LLM

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

## Notes

- The scripts automatically create backups (`.csv.backup`) before writing
- All columns are preserved when updating metadata
- Manual edits to the CSV are preserved (unless using `--force`)

