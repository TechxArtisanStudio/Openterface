# URL Audit Tool for Openterface Documentation

A comprehensive tool to audit all URLs in the Openterface documentation project, supporting multi-language content and various link formats.

## Features

-   **Multi-language Support**: Handles language-specific URLs (e.g., `/en/app`, `/zh/app`)
-   **Multiple Link Formats**: Supports Markdown links, HTML img tags, and href attributes
-   **URL Resolution**: Converts relative paths to absolute URLs
-   **Link Validation**: Checks URL accessibility with rate limiting
-   **Comprehensive Reporting**: Generates detailed CSV reports and summary analysis
-   **Modular Design**: Independent scripts that can be run separately or together

## Quick Start

```bash
# Run complete audit
python scripts/url-audit-tool/url_audit.py

# Run specific modules
python scripts/url-audit-tool/extract_links.py
python scripts/url-audit-tool/resolve_urls.py
python scripts/url-audit-tool/validate_links.py
python scripts/url-audit-tool/generate_reports.py

# View help
python scripts/url-audit-tool/url_audit.py --help
```

## Output Structure

```
scripts/url-audit-tool/
├── data/
│   ├── en/          # English language results
│   ├── zh/          # Chinese language results
│   ├── ja/          # Japanese language results
│   └── ...          # Other languages (loaded from docs/assets/i18n-sites/lang.yml)
├── reports/         # Summary reports and analysis (no language subdirs)
└── logs/           # Processing logs (no language subdirs)
```

## Link Types Detected

-   **Markdown Images**: `![alt](url)`
-   **Markdown Links**: `[text](url)`
-   **HTML Images**: `<img src="url">`
-   **HTML Links**: `href="url"`
-   **Relative Paths**: `/app`, `/product/minikvm/`
-   **External URLs**: `https://assets.openterface.com/...`

## Requirements

-   Python 3.7+
-   requests
-   beautifulsoup4
-   pandas
-   yaml

Install with: `pip install -r scripts/url-audit-tool/requirements.txt`

## Configuration

The tool automatically loads language configuration from `docs/assets/i18n-sites/lang.yml` (single source of truth). Language names are also loaded from the same file for display purposes. This ensures consistency with other i18n tools in the project.
