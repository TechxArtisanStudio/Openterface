"""
Configuration settings for URL Audit Tool
"""

import yaml
from pathlib import Path

# Project paths (now in scripts/url-audit-tool/, so go up 2 levels)
PROJECT_ROOT = Path(__file__).parent.parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"
LANG_YML = DOCS_DIR / "assets" / "i18n-sites" / "lang.yml"

# Base URL from mkdocs.yml
BASE_URL = "https://openterface.com"


def load_i18n_config():
    """Load i18n configuration from docs/assets/i18n-sites/lang.yml (single source of truth)."""
    import sys
    from pathlib import Path
    
    # Add shared loader to path
    shared_dir = PROJECT_ROOT / "scripts" / "i18n-shared"
    if str(shared_dir) not in sys.path:
        sys.path.insert(0, str(shared_dir))
    
    try:
        from lang_loader import I18nConfig
        config = I18nConfig()
        return {
            "default_language": config.default_language,
            "languages": config.languages
        }
    except Exception as e:
        print(f"Warning: Failed to load lang.yml: {e}, using defaults")
        return {
            "default_language": "en",
            "languages": ["en", "zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"]
        }


def load_language_names():
    """Load language names from lang.yml for display purposes."""
    if not LANG_YML.exists():
        return {}
    
    try:
        with open(LANG_YML, 'r', encoding='utf-8') as f:
            lang_data = yaml.safe_load(f) or []
        
        if not isinstance(lang_data, list):
            return {}
        
        lang_names = {}
        for entry in lang_data:
            if isinstance(entry, dict):
                locale = entry.get("locale")
                name = entry.get("name")
                if locale and name:
                    lang_names[locale] = name
        
        return lang_names
    except Exception:
        return {}


# Load i18n configuration
_i18n_config = load_i18n_config()
_languages = _i18n_config.get("languages", ["en"])

# Load language names from lang.yml
_lang_names = load_language_names()

# Default language name mapping (fallback if lang.yml doesn't have a language)
_default_lang_names = {
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

# Create SUPPORTED_LANGUAGES dict from loaded config (for backward compatibility)
# Uses names from lang.yml if available, otherwise falls back to defaults
SUPPORTED_LANGUAGES = {}
for lang_code in _languages:
    lang_name = _lang_names.get(lang_code) or _default_lang_names.get(lang_code, lang_code.title())
    SUPPORTED_LANGUAGES[lang_code] = lang_name

# File patterns to scan
FILE_PATTERNS = {"markdown": ["**/*.md"], "html": ["**/*.html"]}

# Directories to scan
SCAN_DIRECTORIES = [DOCS_DIR / "docs", DOCS_DIR / "overrides"]

# Directories to exclude
EXCLUDE_DIRECTORIES = ["scripts", ".git", "__pycache__", "node_modules"]

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
