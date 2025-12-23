# YouTube Tools - Unified i18n Architecture

## Overview

The YouTube tools follow a **unified i18n pipeline architecture** where content generation is separated from translation.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│              Content Preparation Layer                       │
│  (Various methods to prepare base templates)                 │
└───────────────────┬─────────────────────────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
home-base.html  videos-base.html  future.html
(manual)        (manual)          (any method)
    │               │               │
    └───────────────┼───────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │  scripts/i18n-site-tools/ │
        │  generate_static_pages.py │
        │  (Unified Translation)    │
        └───────────┬───────────────┘
                    │
        ┌───────────┼───────────────┐
        │           │               │
        ▼           ▼               ▼
    home.*.html videos.*.html  future.*.html
    (10 langs)  (10 langs)     (10 langs)
```

## Workflow

### Step 1: Content Preparation (YouTube-specific)

```bash
python scripts/youtube-tools/generate_youtube_website.py --base-template
```

**What it does:**
- Reads `youtube.csv`
- Generates `docs/partials/videos-grid.html` (video cards data partial; no i18n needed)
- Uses `scripts/youtube-tools/youtube-video-card.html` as the card template
- Adds stable card metadata via `data-*` attributes (e.g. `data-date`, `data-language`, `data-product`) so client-side features don’t depend on markup

**Output:**
- `docs/partials/videos-grid.html` - Video card HTML (data from CSV)

### Step 2: Translation Application (Centralized)

```bash
python scripts/i18n-site-tools/generate_static_pages.py --template videos
```

**What it does:**
- Reads `videos-base.html`
- Reads `docs/assets/i18n-sites/videos.json` (translations)
- Reads `docs/assets/i18n-sites/lang.yml` (language config)
- Applies translations for each language
- Removes `data-i18n-key` attributes

**Output:**
- `docs/partials/videos.html` (English)
- `docs/partials/videos.zh.html` (Chinese)
- `docs/partials/videos.ja.html` (Japanese)
- ... (10 languages total)

### All-in-One Command

```bash
python scripts/i18n-site-tools/generate_all_i18n.py
```

**What it does:**
1. Generates `hreflang.html`
2. Runs YouTube content generator (`--base-template`)
3. Runs static pages generator for ALL templates

## File Structure

```
scripts/youtube-tools/
├── youtube.csv                    # Video metadata (source of truth)
├── generate_youtube_website.py   # Content generator
├── update_youtube_csv.py          # Metadata fetcher
└── detect_youtube_language.py     # Language detector

scripts/i18n-site-tools/
├── templates/
│   ├── home-base.html            # Manual template
│   └── videos-base.html          # Manual template (layout + i18n keys; includes videos-grid.html)
├── generate_static_pages.py      # Unified translation engine
└── generate_all_i18n.py          # Orchestrator

docs/
├── assets/i18n-sites/
│   ├── lang.yml                  # Language config (SSOT)
│   ├── home.json                 # Home page translations
│   └── videos.json               # Videos page translations
├── overrides/
│   ├── home.*.html               # Generated home pages
└── partials/
    ├── hreflang.html             # Auto-generated SEO links
    ├── videos-grid.html          # Video cards (no i18n)
    └── videos.*.html             # Generated videos partials (10 languages)
```

## Key Principles

### 1. Separation of Concerns
- **Content Generation**: YouTube tools handle CSV → HTML structure
- **Translation**: i18n tools handle placeholders → language-specific text

### 2. Single Source of Truth
- `youtube.csv` - Video data
- `lang.yml` - Language configuration
- `videos.json` - UI translations

### 3. DRY (Don't Repeat Yourself)
- One translation system for ALL pages
- No duplicate i18n logic in each tool

### 4. Extensibility
- Any tool can prepare base templates
- All follow the same `data-i18n-key` pattern
- Centralized system handles translations

## Adding a New Page

To add a new page following this architecture:

1. **Create base template** (manual or programmatic):
```html
<h1 data-i18n-key="title">My Page</h1>
<p data-i18n-key="description">Description here</p>
```

2. **Save as** `scripts/i18n-site-tools/templates/mypage-base.html`

3. **Create translations** in `docs/assets/i18n-sites/mypage.json`:
```json
{
  "supported_languages": ["en", "zh", "ja", ...],
  "translations": {
    "en": {
      "title": "My Page",
      "description": "Description here"
    },
    "zh": {
      "title": "我的页面",
      "description": "这里的描述"
    }
  }
}
```

4. **Generate**:
```bash
python scripts/i18n-site-tools/generate_static_pages.py --template mypage
```

Done! You get `mypage.*.html` for all languages.

## Benefits

✅ **Architectural Consistency**: All pages use same pattern
✅ **Easier Maintenance**: One system to understand
✅ **Centralized Translations**: Single place for all i18n
✅ **Better SEO**: Static HTML for each language
✅ **Validation**: Automatic language validation
✅ **Extensible**: Easy to add new pages
✅ **Clean Separation**: Content ≠ Translation

