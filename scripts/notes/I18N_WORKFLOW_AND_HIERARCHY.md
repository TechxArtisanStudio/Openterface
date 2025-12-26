# i18n Workflow and Hierarchy Documentation

## Overview

This document provides a comprehensive guide to the internationalization (i18n) workflow and file hierarchy in the Openterface website project. Understanding this structure will help you optimize and fine-tune the i18n system.

## Table of Contents

1. [File Hierarchy](#file-hierarchy)
2. [Data Flow](#data-flow)
3. [Core Components](#core-components)
4. [Tool Categories](#tool-categories)
5. [Workflow Diagrams](#workflow-diagrams)
6. [Optimization Opportunities](#optimization-opportunities)

---

## File Hierarchy

### Single Source of Truth

```
docs/assets/i18n-sites/
├── lang.yml                    # ⭐ SINGLE SOURCE OF TRUTH
│   ├── Language definitions (locale, name, build flag)
│   ├── Site names per language
│   └── Navigation translations (nav_translations)
│
├── home.json                   # Home page translations
├── videos.json                 # Videos page translations
└── forms.json                  # Form translations
```

### Configuration Files

```
Project Root/
├── mkdocs.yml                  # MkDocs config (managed by scripts)
│   └── plugins.i18n.languages # Synced from lang.yml via manage_i18n.py
│
└── docs/
    ├── assets/
    │   ├── i18n-sites/         # All i18n configuration files
    │   │   ├── lang.yml        # ⭐ Primary config
    │   │   ├── *.json          # Template translations
    │   │   └── ...
    │   └── javascripts/
    │       └── language-select.js  # Frontend language switcher
    │
    ├── overrides/              # Generated static HTML pages
    │   ├── home.html           # English home page
    │   ├── home.zh.html        # Chinese home page
    │   ├── home.ja.html        # Japanese home page
    │   └── ...                 # Other languages
    │
    └── partials/               # Generated content fragments
        ├── hreflang.html       # Auto-generated SEO links
        ├── videos.html         # English videos
        ├── videos.zh.html      # Chinese videos
        └── ...                 # Other languages
```

### Script Organization

```
scripts/
├── i18n-shared/                # ⭐ Shared utilities
│   ├── __init__.py
│   └── lang_loader.py          # I18nConfig class (reads lang.yml)
│
├── i18n-site-tools/            # Static page generation
│   ├── i18n_config.py          # Wrapper (uses i18n-shared)
│   ├── generate_static_pages.py # Generates HTML from templates
│   ├── generate_all_i18n.py    # Convenience script
│   └── templates/              # HTML templates with data-i18n-key
│
├── i18n-docs-tools/            # Documentation translation management
│   ├── audit_translations.py   # Check translation coverage
│   ├── generate_prompts.py    # Generate LLM translation prompts
│   ├── cleanup_translations.py # Remove orphaned translations
│   ├── clean_file_variants.py  # Clean language variant files
│   └── workflow.py             # Unified workflow manager
│
├── manage_i18n.py              # Sync lang.yml → mkdocs.yml
├── sync_redirects.py           # Extract languages from lang.yml
│
├── url-audit-tool/             # Uses lang.yml for language config
├── update-post-tool/           # Uses lang.yml for language config
└── youtube-tools/              # Uses I18nConfig from i18n-site-tools
```

---

## Data Flow

### 1. Configuration Flow

```
lang.yml (Single Source of Truth)
    │
    ├─→ manage_i18n.py ──→ mkdocs.yml (i18n plugin config)
    │
    └─→ i18n-shared/lang_loader.py ──→ I18nConfig class
            │
            ├─→ i18n-site-tools (static page generation)
            ├─→ i18n-docs-tools (translation management)
            ├─→ url-audit-tool (language validation)
            ├─→ update-post-tool (language config)
            └─→ youtube-tools (language config)
```

### 2. Static Page Generation Flow

```
Templates (HTML with data-i18n-key)
    │
    ├─→ Translation JSON (home.json, videos.json)
    │
    └─→ generate_static_pages.py
            │
            ├─→ Reads lang.yml (via I18nConfig)
            ├─→ Validates JSON has all languages
            ├─→ Generates HTML for each language
            │
            └─→ Output:
                ├─→ docs/overrides/home.*.html
                └─→ docs/partials/videos.*.html
```

### 3. Documentation Translation Flow

```
Markdown Files (docs/**/*.md)
    │
    ├─→ audit_translations.py
    │   └─→ i18n_audit.csv (coverage matrix)
    │
    ├─→ generate_prompts.py
    │   └─→ prompts/*.llm-task.txt (translation tasks)
    │
    └─→ cleanup_translations.py
        └─→ Removes orphaned translations
```

---

## Core Components

### 1. lang.yml (Single Source of Truth)

**Location:** `docs/assets/i18n-sites/lang.yml`

**Purpose:** Central configuration file containing:
- Language definitions (locale, name, build flag)
- Site names per language
- Navigation menu translations

**Structure:**
```yaml
- locale: zh
  name: 简体中文
  build: true
  site_name: "Openterface | 连接接口，开启无限可能"
  nav_translations:
    Home: 首页
    FAQs: 常见问题
    # ... all navigation items
```

**Key Properties:**
- `locale`: Language code (ISO 639-1)
- `name`: Native language name
- `build`: Whether to include in builds (true/false)
- `site_name`: Site title for this language
- `nav_translations`: Complete navigation menu translations

### 2. I18nConfig Class

**Location:** `scripts/i18n-shared/lang_loader.py`

**Purpose:** Shared utility class that:
- Loads `lang.yml` directly
- Extracts languages with `build: true`
- Gets default language from `mkdocs.yml` theme.language
- Provides validation and hreflang generation

**Usage:**
```python
from lang_loader import I18nConfig

config = I18nConfig()
languages = config.languages  # ['en', 'zh', 'ja', ...]
default = config.default_language  # 'en'
config.validate_json_languages(json_langs, "source.json")
```

### 3. Translation JSON Files

**Location:** `docs/assets/i18n-sites/*.json`

**Purpose:** Template-specific translations for static page generation

**Structure:**
```json
{
  "supported_languages": ["en", "zh", "ja", ...],
  "translations": {
    "en": {
      "key1": "English text",
      "key2": "More text"
    },
    "zh": {
      "key1": "中文文本",
      "key2": "更多文本"
    }
  }
}
```

**Files:**
- `home.json`: Home page translations
- `videos.json`: Videos page translations
- `forms.json`: Form translations

---

## Tool Categories

### Category 1: Configuration Management

#### `scripts/manage_i18n.py`
- **Purpose:** Sync `lang.yml` → `mkdocs.yml`
- **Usage:**
  ```bash
  python scripts/manage_i18n.py add        # Add all languages
  python scripts/manage_i18n.py remove     # Remove all except English
  python scripts/manage_i18n.py list       # Show current config
  ```
- **When to use:** After modifying `lang.yml`

### Category 2: Static Page Generation

#### `scripts/i18n-site-tools/generate_static_pages.py`
- **Purpose:** Generate SEO-friendly static HTML from templates
- **Input:**
  - HTML templates with `data-i18n-key` attributes
  - Translation JSON files
  - `lang.yml` (via I18nConfig)
- **Output:**
  - `docs/overrides/home.*.html` (per language)
  - `docs/partials/videos.*.html` (per language)
  - `docs/overrides/partials/hreflang.html`
- **Usage:**
  ```bash
  python scripts/i18n-site-tools/generate_static_pages.py --all
  python scripts/i18n-site-tools/generate_static_pages.py --template home
  ```

#### `scripts/i18n-site-tools/generate_all_i18n.py`
- **Purpose:** Convenience script to generate all i18n content
- **Steps:**
  1. Generate hreflang partial
  2. Generate videos from CSV
  3. Generate all static pages
- **Usage:**
  ```bash
  python scripts/i18n-site-tools/generate_all_i18n.py
  ```

### Category 3: Documentation Translation Management

#### `scripts/i18n-docs-tools/audit_translations.py`
- **Purpose:** Audit translation coverage for Markdown files
- **Output:** CSV file showing which files have translations for which languages
- **Usage:**
  ```bash
  python scripts/i18n-docs-tools/audit_translations.py --docs docs
  python scripts/i18n-docs-tools/audit_translations.py --only-missing
  python scripts/i18n-docs-tools/audit_translations.py --fail-on-missing
  ```

#### `scripts/i18n-docs-tools/generate_prompts.py`
- **Purpose:** Generate LLM prompts for missing translations
- **Output:** Markdown task files in `prompts/` directory
- **Usage:**
  ```bash
  python scripts/i18n-docs-tools/generate_prompts.py --docs docs --overwrite
  ```

#### `scripts/i18n-docs-tools/cleanup_translations.py`
- **Purpose:** Remove orphaned translations (no English base)
- **Usage:**
  ```bash
  python scripts/i18n-docs-tools/cleanup_translations.py --dry-run
  python scripts/i18n-docs-tools/cleanup_translations.py
  ```

#### `scripts/i18n-docs-tools/workflow.py`
- **Purpose:** Unified workflow manager
- **Commands:**
  - `refresh`: Run complete workflow (audit + prompts + report)
  - `audit`: Run translation coverage audit
  - `prompts`: Generate LLM prompts
  - `report`: Show coverage report
  - `status`: Show current status
- **Usage:**
  ```bash
  python scripts/i18n-docs-tools/workflow.py refresh
  python scripts/i18n-docs-tools/workflow.py audit --only-missing
  ```

### Category 4: Supporting Tools

#### `scripts/url-audit-tool/`
- **Uses:** `lang.yml` via I18nConfig for language validation

#### `scripts/update-post-tool/`
- **Uses:** `lang.yml` via I18nConfig for language config

#### `scripts/youtube-tools/`
- **Uses:** I18nConfig from i18n-site-tools for language validation

---

## Workflow Diagrams

### Complete i18n Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    lang.yml (SSOT)                          │
│  - Language definitions                                     │
│  - Navigation translations                                  │
│  - Site names                                               │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
┌─────────────────┐    ┌──────────────────────┐
│ manage_i18n.py  │    │ I18nConfig (shared)  │
│                 │    │                      │
│ Syncs to:       │    │ Used by:             │
│ - mkdocs.yml    │    │ - i18n-site-tools    │
└─────────────────┘    │ - i18n-docs-tools    │
                       │ - url-audit-tool     │
                       │ - update-post-tool   │
                       │ - youtube-tools      │
                       └──────────────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
    ┌──────────────────┐ ┌──────────────┐ ┌──────────────┐
    │ Static Pages     │ │ Docs Audit   │ │ Other Tools  │
    │ Generation       │ │ & Management │ │              │
    │                  │ │              │ │              │
    │ Templates +      │ │ Markdown     │ │ Language     │
    │ Translation JSON │ │ Files        │ │ Validation   │
    │                  │ │              │ │              │
    │ → HTML files     │ │ → CSV audit  │ │ → Config     │
    │ → hreflang.html  │ │ → Prompts    │ │              │
    └──────────────────┘ └──────────────┘ └──────────────┘
```

### Static Page Generation Workflow

```
┌──────────────────┐
│ HTML Templates   │  (with data-i18n-key attributes)
│ - home-base.html │
│ - videos-base... │
└────────┬─────────┘
         │
         │ + ┌──────────────────┐
         │   │ Translation JSON  │
         │   │ - home.json       │
         │   │ - videos.json     │
         │   └───────────────────┘
         │
         │ + ┌──────────────────┐
         │   │ lang.yml          │
         │   │ (via I18nConfig)  │
         │   └───────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ generate_static_pages.py    │
│                             │
│ 1. Load template            │
│ 2. Load translations        │
│ 3. Validate languages       │
│ 4. Replace data-i18n-key    │
│ 5. Generate per language   │
└─────────────┬───────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ Generated HTML      │
    │                     │
    │ docs/overrides/     │
    │ - home.html         │
    │ - home.zh.html      │
    │ - home.ja.html      │
    │ ...                 │
    │                     │
    │ docs/partials/      │
    │ - videos.html       │
    │ - videos.zh.html    │
    │ ...                 │
    │                     │
    │ docs/overrides/     │
    │ partials/           │
    │ - hreflang.html     │
    └─────────────────────┘
```

### Documentation Translation Workflow

```
┌──────────────────┐
│ Markdown Files   │
│ docs/**/*.md     │
│                  │
│ - index.md       │
│ - about.md       │
│ - product/...    │
└────────┬─────────┘
         │
         ▼
┌─────────────────────────────┐
│ audit_translations.py       │
│                             │
│ Scans for:                  │
│ - base files (*.md)          │
│ - variants (*.lang.md)      │
│                             │
│ Output: i18n_audit.csv      │
└─────────────┬───────────────┘
              │
              ▼
    ┌─────────────────────┐
    │ Coverage Matrix     │
    │ (CSV)               │
    │                     │
    │ File | en | zh | ja │
    │ ...  | 1  | 1  | 0  │
    └─────────────┬───────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌──────────────┐   ┌──────────────────┐
│ generate_    │   │ cleanup_         │
│ prompts.py   │   │ translations.py  │
│              │   │                  │
│ Creates LLM  │   │ Removes orphaned │
│ task files   │   │ translations     │
└──────────────┘   └──────────────────┘
```

---

## Optimization Opportunities

### Current Strengths

1. **Single Source of Truth:** `lang.yml` eliminates duplication
2. **Shared Utilities:** `i18n-shared/lang_loader.py` provides consistent access
3. **Separation of Concerns:** Different tools for different purposes
4. **Build-time Generation:** SEO-friendly static HTML

### Potential Optimizations

#### 1. Consolidate Translation JSON Structure

**Current:** Separate JSON files per template (home.json, videos.json, forms.json)

**Opportunity:** Consider a unified structure or shared keys:
```json
{
  "shared": {
    "en": { "common_key": "..." },
    "zh": { "common_key": "..." }
  },
  "templates": {
    "home": { ... },
    "videos": { ... }
  }
}
```

#### 2. Automate Translation Validation

**Current:** Manual audit and prompt generation

**Opportunity:** 
- Add pre-commit hooks to validate translations
- Auto-generate prompts in CI/CD
- Integrate with translation services

#### 3. Template Management

**Current:** Templates in `i18n-site-tools/templates/`

**Opportunity:**
- Consider moving to `docs/templates/` for better organization
- Create template registry/validation
- Add template versioning

#### 4. Language Configuration

**Current:** Default language from `mkdocs.yml` theme.language

**Opportunity:**
- Add `default_language` field to `lang.yml`
- Remove dependency on `mkdocs.yml` for default language
- Make `lang.yml` fully self-contained

#### 5. Workflow Integration

**Current:** Multiple separate scripts

**Opportunity:**
- Create unified CLI tool (`i18n-cli`) with subcommands
- Add workflow orchestration script
- Integrate with build process automatically

#### 6. Performance Optimization

**Current:** Scripts load `lang.yml` independently

**Opportunity:**
- Cache `lang.yml` parsing
- Parallelize static page generation
- Incremental generation (only changed languages)

#### 7. Documentation

**Current:** Documentation scattered across multiple README files

**Opportunity:**
- Centralize in this document
- Add interactive diagrams
- Create quick reference guide

---

## Quick Reference

### Adding a New Language

1. **Edit `docs/assets/i18n-sites/lang.yml`**
   ```yaml
   - locale: ru
     name: Русский
     build: true
     site_name: "..."
     nav_translations: { ... }
   ```

2. **Sync to mkdocs.yml**
   ```bash
   python scripts/manage_i18n.py add
   ```

3. **Add translations to JSON files**
   - `docs/assets/i18n-sites/home.json`
   - `docs/assets/i18n-sites/videos.json`
   - `docs/assets/i18n-sites/forms.json`

4. **Update frontend language switcher**
   - `docs/assets/javascripts/language-select.js`

5. **Regenerate static pages**
   ```bash
   python scripts/i18n-site-tools/generate_all_i18n.py
   ```

### Common Workflows

#### Daily Development
```bash
# Generate static pages
python scripts/i18n-site-tools/generate_all_i18n.py

# Run MkDocs
python run.py
```

#### Translation Management
```bash
# Audit coverage
python scripts/i18n-docs-tools/workflow.py audit

# Generate prompts for missing translations
python scripts/i18n-docs-tools/workflow.py prompts

# Full workflow
python scripts/i18n-docs-tools/workflow.py refresh
```

#### Adding New Template
1. Create template in `scripts/i18n-site-tools/templates/`
2. Create translation JSON in `docs/assets/i18n-sites/`
3. Add to `template_output_dirs` in `generate_static_pages.py`
4. Run generator

---

## File Dependencies

### Critical Path

```
lang.yml
  ↓
I18nConfig (i18n-shared/lang_loader.py)
  ↓
├─→ i18n-site-tools → Static HTML generation
├─→ i18n-docs-tools → Translation management
└─→ Other tools → Language validation
```

### Build Dependencies

```
Before MkDocs build:
  1. lang.yml exists
  2. manage_i18n.py syncs to mkdocs.yml
  3. generate_static_pages.py creates HTML files
  4. hreflang.html generated
```

---

## Troubleshooting

### Issue: Missing translations in static pages

**Check:**
1. Does `lang.yml` have the language with `build: true`?
2. Does the JSON file have translations for that language?
3. Run validation: `I18nConfig.validate_json_languages()`

### Issue: mkdocs.yml out of sync

**Solution:**
```bash
python scripts/manage_i18n.py add
```

### Issue: Generated HTML missing translations

**Check:**
1. Template has `data-i18n-key` attributes?
2. JSON file has matching keys?
3. Language is in both `lang.yml` and JSON?

---

## Conclusion

The i18n system is well-structured with a clear hierarchy:

1. **Single Source of Truth:** `lang.yml` at the top
2. **Shared Utilities:** `i18n-shared/` for common functionality
3. **Specialized Tools:** Separate tools for different purposes
4. **Clear Data Flow:** From config → generation → output

The main optimization opportunities are:
- Consolidating translation JSON structure
- Automating validation workflows
- Improving template management
- Creating unified CLI interface

This structure provides a solid foundation for maintaining and scaling the multilingual website.

