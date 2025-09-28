"""
Configuration settings for URL Audit Tool
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"

# Base URL from mkdocs.yml
BASE_URL = "https://openterface.com"

# Supported languages (from mkdocs.yml i18n configuration)
SUPPORTED_LANGUAGES = {
    "en": "English",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ro": "Romanian",
}

# File patterns to scan
FILE_PATTERNS = {"markdown": ["**/*.md"], "html": ["**/*.html"]}

# Directories to scan
SCAN_DIRECTORIES = [DOCS_DIR / "docs", DOCS_DIR / "overrides"]

# Directories to exclude
EXCLUDE_DIRECTORIES = ["i18n-tools", "scripts", ".git", "__pycache__", "node_modules"]

# Output directories
OUTPUT_DIR = Path(__file__).parent / "data"
REPORTS_DIR = Path(__file__).parent / "reports"
LOGS_DIR = Path(__file__).parent / "logs"

# Create output directories
for directory in [OUTPUT_DIR, REPORTS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Create language subdirectories only for data directory
for lang in SUPPORTED_LANGUAGES.keys():
    (OUTPUT_DIR / lang).mkdir(exist_ok=True)

# Link validation settings
VALIDATION_CONFIG = {
    "timeout": 10,
    "max_retries": 3,
    "delay_between_requests": 0.5,
    "user_agent": "Openterface-URL-Audit-Tool/1.0",
    "skip_validation_domains": ["localhost", "127.0.0.1", "0.0.0.0"],
}

# Regex patterns for different link types
LINK_PATTERNS = {
    "markdown_image": r"!\[([^\]]*)\]\(([^)]+)\)",
    "markdown_link": r"\[([^\]]*)\]\(([^)]+)\)",
    "html_img_src": r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>',
    "html_href": r'href=["\']([^"\']+)["\']',
    "url": r"https?://[^\s\)]+",
}

# CSV column definitions
CSV_COLUMNS = {
    "extracted": [
        "file_path",
        "line_number",
        "link_type",
        "link_text",
        "raw_url",
        "is_external",
        "is_image",
        "context",
    ],
    "resolved": [
        "file_path",
        "line_number",
        "link_type",
        "link_text",
        "raw_url",
        "resolved_url",
        "full_url",
        "domain",
        "path",
        "language",
        "is_external",
        "is_image",
        "context",
    ],
    "validated": [
        "url",
        "status_code",
        "response_time",
        "error_message",
        "is_valid",
        "redirect_url",
        "content_type",
        "file_size",
        "js_redirect_detected",
        "language",
        "usage_count",
        "file_locations",
    ],
}
