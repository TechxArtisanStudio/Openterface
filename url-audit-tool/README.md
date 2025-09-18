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
python url_audit.py

# Run specific modules
python extract_links.py
python resolve_urls.py
python validate_links.py
python generate_reports.py

# View help
python url_audit.py --help
```

## Output Structure

```
url-audit-tool/
├── data/
│   ├── en/          # English language results
│   ├── zh/          # Chinese language results
│   ├── ja/          # Japanese language results
│   └── ...          # Other languages
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

Install with: `pip install -r requirements.txt`
