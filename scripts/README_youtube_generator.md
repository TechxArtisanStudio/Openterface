# YouTube Reviews Generator

This script automatically generates YouTube review pages (`youtube.md`) from `.youtube.list` files found in product directories.

## Features

- **Automatic Discovery**: Scans all product directories for `.youtube.list` files
- **Metadata Preservation**: Parses existing `youtube.md` files to preserve channel names, titles, and thumbnails
- **Enhanced Formatting**: Maintains the original format while adding new videos
- **Language Detection**: Automatically detects video language based on title and channel name
- **Offline Mode**: Can work without internet connection using existing metadata
- **Fallback Support**: Gracefully handles network issues and missing metadata

## Usage

### Quick Start (with proxy)
```bash
# Use the wrapper script for easy proxy setup
./scripts/run_youtube_generator.sh

# With options
./scripts/run_youtube_generator.sh --dry-run --verbose
```

### Manual Usage

```bash
# Basic usage - scans all products and generates/updates youtube.md files
python scripts/generate_youtube_reviews.py

# Dry run - see what would be generated without making changes
python scripts/generate_youtube_reviews.py --dry-run

# Verbose output - see detailed processing information
python scripts/generate_youtube_reviews.py --verbose

# Offline mode - use existing metadata only, no network requests
python scripts/generate_youtube_reviews.py --offline

# With proxy support
python scripts/generate_youtube_reviews.py --proxy http://127.0.0.1:1087

# Using environment variables for proxy
export http_proxy=http://127.0.0.1:1087
export https_proxy=http://127.0.0.1:1087
python scripts/generate_youtube_reviews.py

# Combine options
python scripts/generate_youtube_reviews.py --dry-run --verbose --proxy http://127.0.0.1:1087
```

## File Structure

The script expects this structure:
```
docs/product/
├── minikvm/
│   └── reviews/
│       ├── .youtube.list          # List of YouTube URLs
│       └── youtube.md             # Generated review page
├── kvm-go/
│   └── reviews/
│       ├── .youtube.list
│       └── youtube.md
└── ...
```

## .youtube.list Format

Each `.youtube.list` file should contain one YouTube URL per line:
```
https://www.youtube.com/watch?v=l5e1wHwZ__c
https://www.youtube.com/watch?v=sKDYsKBv90A
https://youtu.be/ZZ5P6MnBcHw
```

## Generated Output

The script generates `youtube.md` files in this format:
```markdown
# YouTube

- <a href="https://www.youtube.com/@ChannelName"><img src="thumbnail_url" alt="" width="28" style="border-radius: 50%; vertical-align: middle;" onerror="this.style.display='none'"></a> **Channel Name**: [Video Title](https://www.youtube.com/watch?v=VIDEO_ID) | Language
```

## Language Detection

The script automatically detects language based on:
- Character sets (Chinese, Japanese, Korean, etc.)
- Special characters (Spanish, French, Italian, etc.)
- Defaults to English if no specific patterns found

## Error Handling

- Network timeouts are handled gracefully
- Missing metadata falls back to placeholder values
- Invalid URLs are skipped with warnings
- Existing files are parsed to preserve metadata

## Requirements

- Python 3.6+
- requests library (for online mode)
- No additional dependencies for offline mode
