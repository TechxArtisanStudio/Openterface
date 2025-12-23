# i18n Site Tools

Build-time static HTML generator for multilingual SEO-optimized pages.

## Overview

This tool generates static HTML files from templates with `data-i18n-key` attributes and translation JSON files. Unlike client-side JavaScript translation, this approach creates fully translated HTML files at build time, making them perfectly indexable by search engines.

## Architecture

```
scripts/scripts/i18n-site-tools/
├── generate_static_pages.py    # Main generator script
├── templates/                   # HTML templates with data-i18n-key attributes
│   └── home-base.html          # Home page template
└── README.md                    # This file

Translation files:
└── docs/assets/i18n-sites/
    └── home.json                # Home page translations for all languages
```

## Why Build-Time Generation?

### SEO Benefits

- **Perfect Indexing**: Search engines see fully translated static HTML
- **No JavaScript Required**: Crawlers don't need to execute JavaScript
- **Language-Specific URLs**: Each language URL (`/zh/`, `/ja/`, etc.) serves its own file
- **Performance**: No client-side translation overhead

### Maintenance Benefits

- **Single Source of Truth**: One template file for all languages
- **Centralized Translations**: All translations in one JSON file
- **Easy Updates**: Change template or translations, regenerate all languages

## Usage

### Generate Home Page (All Languages)

```bash
python scripts/scripts/i18n-site-tools/generate_static_pages.py --template home
```

This generates:
- `docs/overrides/home.html` (English)
- `docs/overrides/home.zh.html` (Chinese)
- `docs/overrides/home.ja.html` (Japanese)
- `docs/overrides/home.ko.html` (Korean)
- `docs/overrides/home.fr.html` (French)
- `docs/overrides/home.de.html` (German)
- `docs/overrides/home.it.html` (Italian)
- `docs/overrides/home.es.html` (Spanish)
- `docs/overrides/home.pt.html` (Portuguese)
- `docs/overrides/home.ro.html` (Romanian)

### Generate Specific Language

```bash
python scripts/scripts/i18n-site-tools/generate_static_pages.py --template home --language zh
```

### Generate All Templates

```bash
python scripts/scripts/i18n-site-tools/generate_static_pages.py --all
```

## How It Works

### 1. Template with i18n Attributes

```html
<div class="carousel-category" data-i18n-key="slide1_category">KVM-GO Series</div>
<h1 class="carousel-headline" data-i18n-key="slide1_headline">The Ultra-Compact KVM That Fits on Keychain</h1>
```

### 2. Translation JSON

```json
{
  "supported_languages": ["en", "zh", "ja", ...],
  "translations": {
    "en": {
      "slide1_category": "KVM-GO Series",
      "slide1_headline": "The Ultra-Compact KVM That Fits on Keychain"
    },
    "zh": {
      "slide1_category": "KVM-GO 系列",
      "slide1_headline": "超迷你便携式 KVM，可随身挂在钥匙扣上"
    }
  }
}
```

### 3. Generated Static HTML (Chinese)

```html
<div class="carousel-category">KVM-GO 系列</div>
<h1 class="carousel-headline">超迷你便携式 KVM，可随身挂在钥匙扣上</h1>
```

Note: `data-i18n-key` attributes are removed in the final output.

## Adding a New Template

### 1. Create Template File

Create `scripts/i18n-site-tools/templates/your-page-base.html` with `data-i18n-key` attributes:

```html
<div data-i18n-key="heading">English Text</div>
<p data-i18n-key="description">Description here</p>
```

### 2. Create Translation JSON

Create `docs/assets/i18n-sites/your-page.json`:

```json
{
  "supported_languages": ["en", "zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro"],
  "translations": {
    "en": {
      "heading": "English Heading",
      "description": "English description"
    },
    "zh": {
      "heading": "中文标题",
      "description": "中文描述"
    }
    // ... other languages
  }
}
```

### 3. Generate

```bash
python scripts/scripts/i18n-site-tools/generate_static_pages.py --template your-page
```

## Adding a New Language

### 1. Update Translation JSON

Add the new language code to `supported_languages` and provide translations in all relevant JSON files:

```json
{
  "supported_languages": ["en", "zh", "ja", "ko", "fr", "de", "it", "es", "pt", "ro", "nl"],
  "translations": {
    "nl": {
      "heading": "Nederlandse Kop",
      "description": "Nederlandse beschrijving"
    }
  }
}
```

### 2. Regenerate

```bash
python scripts/scripts/i18n-site-tools/generate_static_pages.py --all
```

### 3. Configure MkDocs

Add the new language to your `mkdocs.yml` i18n plugin configuration.

## Workflow

### When to Regenerate

Run the generator when:

1. **Template Structure Changes**: Modified `templates/*-base.html`
2. **Translation Updates**: Updated `docs/assets/i18n-sites/*.json`
3. **Before Deployment**: Ensure all static files are up-to-date

### Recommended Git Workflow

```bash
# 1. Edit template or translations
vim scripts/i18n-site-tools/templates/home-base.html
vim docs/assets/i18n-sites/home.json

# 2. Regenerate static files
python scripts/scripts/i18n-site-tools/generate_static_pages.py --template home

# 3. Commit both source and generated files
git add scripts/i18n-site-tools/ docs/assets/i18n-sites/ docs/overrides/
git commit -m "Update home page translations"
```

## Integration with CI/CD

Add to your build pipeline:

```yaml
# .github/workflows/deploy.yml
- name: Generate Static i18n Pages
  run: |
    python scripts/scripts/i18n-site-tools/generate_static_pages.py --all
    
- name: Build MkDocs Site
  run: mkdocs build
```

## Comparison with Client-Side i18n

| Feature | Build-Time (This Tool) | Client-Side (JavaScript) |
|---------|----------------------|--------------------------|
| SEO | ✅ Perfect | ❌ Limited |
| Performance | ✅ No runtime overhead | ❌ Translation delay |
| Crawlers | ✅ See translated content | ❌ See only default language |
| Maintainability | ✅ Single template | ❌ Multiple HTML files or complex JS |
| Build Time | ⚠️ Requires generation step | ✅ No build step |
| Dynamic Content | ❌ Not suitable | ✅ Good for frequently changing content |

## Best Practices

1. **Always commit generated files**: The static HTML files are the source of truth for production
2. **Run generator before commits**: Ensure generated files are in sync with templates
3. **Test all languages**: Verify each language file after generation
4. **Keep translations complete**: Ensure all keys exist in all languages (fallback to English if missing)
5. **Use semantic keys**: Name keys descriptively (e.g., `slide1_headline` not `text1`)

## Language Configuration

All supported languages are configured in a single source of truth:

**File**: `docs/assets/i18n-sites/lang.yml`

The `lang.yml` file contains language definitions with `locale`, `name`, and `build` fields.
Languages with `build: true` (or no `build` field) are included in the site generation.

### Adding a New Language

1. Add language entry to `lang.yml` with `build: true`
2. Add translations to relevant JSON files (`home.json`, `videos.json`)
3. Regenerate all pages: `python scripts/i18n-site-tools/generate_static_pages.py --all`

### Validation

The generator automatically validates that JSON translation files include all languages from `lang.yml`:
- **Missing languages**: Shows warning, generates only available languages
- **Extra languages**: Shows info message, includes them in generation

This ensures consistency across the site while allowing flexibility during translation work.

### Automatic hreflang Generation

The system automatically generates `docs/partials/hreflang.html` from `lang.yml`. This file is included in `docs/overrides/main.html` in the `extrahead` block:

```html
<!-- Language Alternates (hreflang for SEO) -->
{% include "partials/hreflang.html" %}
```

**All pages automatically inherit hreflang** through the template chain:
- Regular markdown pages → main.html → base.html
- Custom override pages → main.html → base.html (via `{{ super() }}`)

No need to add hreflang to individual page templates - it's automatic!

## Dependencies

- **Python 3.8+**
- **PyYAML**: For reading lang.yml configuration

Install dependencies:

```bash
pip install pyyaml
```

No external dependencies required for HTML generation! The generator uses Python's built-in `re` module for regex-based text replacement, which preserves Jinja2 template syntax perfectly.

## Troubleshooting

### "Template not found" Error

Ensure template file exists: `scripts/i18n-site-tools/templates/your-template-base.html`

### "i18n configuration file not found" Error

Ensure JSON file exists: `docs/assets/i18n-sites/your-template.json`

### Missing Translations

Check JSON file has all required keys for all languages. Missing keys will use the default text from the template.

### HTML Structure Broken

BeautifulSoup may reformat HTML. If issues occur:
1. Check template HTML is well-formed
2. Verify no unclosed tags
3. Use `html.parser` instead of `lxml` if needed (modify script)

## Support

For issues or questions:
1. Check this README
2. Review the plan document
3. Contact the development team

