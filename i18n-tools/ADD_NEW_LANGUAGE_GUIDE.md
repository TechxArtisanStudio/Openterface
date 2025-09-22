# Adding New Language Support to Openterface Website

This guide outlines all the configuration files and scripts that need to be modified when adding a new language to the Openterface website project.

## Overview

The Openterface website uses MkDocs with the `mkdocs-static-i18n` plugin for internationalization. The project supports 10 languages currently: English (en), Chinese (zh), Japanese (ja), Korean (ko), French (fr), German (de), Italian (it), Spanish (es), Portuguese (pt), and Romanian (ro).

## Files That Need Modification

### 1. Core Configuration Files

#### `lang.yml` (Primary Language Definition)
- **Location**: `/lang.yml`
- **Purpose**: Contains all language definitions, names, and navigation translations
- **Action Required**: Add new language entry with:
  - `locale`: Language code (e.g., `ru`, `ar`, `hi`)
  - `name`: Native language name
  - `build: true`
  - `nav_translations`: Complete navigation menu translations

**Example for Russian:**
```yaml
- locale: ru
  name: Русский
  build: true
  nav_translations:
    Home: Главная
    FAQs: Часто задаваемые вопросы
    Product: Продукт
    # ... all navigation items
```

#### `mkdocs.yml` (MkDocs Configuration)
- **Location**: `/mkdocs.yml`
- **Purpose**: Active MkDocs configuration with i18n plugin settings
- **Action Required**: 
  - Language configuration is managed automatically by `scripts/manage_i18n.py`
  - **DO NOT** manually edit i18n languages in this file
  - Use the management script instead

#### `i18n-tools/i18n.yml` (i18n Tools Configuration)
- **Location**: `/i18n-tools/i18n.yml`
- **Purpose**: Configuration for i18n workflow tools
- **Action Required**: Add new language code to the `languages` list

### 2. JavaScript Files

#### `docs/assets/javascripts/language-select.js`
- **Location**: `/docs/assets/javascripts/language-select.js`
- **Purpose**: Frontend language selection functionality
- **Action Required**: 
  - Add new language to `langMap` object
  - Add language name to `langNames` object

**Example for Russian:**
```javascript
const langMap = {
  'en': baseUrl + '/',
  'de': baseUrl + '/de/',
  'fr': baseUrl + '/fr/',
  // ... existing languages
  'ru': baseUrl + '/ru/',  // ADD THIS
};

const langNames = { 
  de: "Deutsch", 
  en: "English", 
  // ... existing languages
  ru: "Русский"  // ADD THIS
};
```

### 3. Management Scripts

#### `scripts/manage_i18n.py`
- **Location**: `/scripts/manage_i18n.py`
- **Purpose**: Manages language configuration between `lang.yml` and `mkdocs.yml`
- **Action Required**: No modification needed - script automatically reads from `lang.yml`

#### `run.py`
- **Location**: `/run.py`
- **Purpose**: Main script for running MkDocs with i18n management
- **Action Required**: No modification needed - uses `manage_i18n.py`

#### `run-i18n.sh` and `run-en-only.sh`
- **Location**: `/run-i18n.sh`, `/run-en-only.sh`
- **Purpose**: Convenience scripts for running with/without i18n
- **Action Required**: No modification needed

### 4. i18n Tools Scripts

#### `i18n-tools/i18n_1_from_mkdocs.py`
- **Purpose**: Generates i18n config from mkdocs.yml
- **Action Required**: No modification needed - reads from mkdocs.yml

#### `i18n-tools/i18n_2_audit.py`
- **Purpose**: Audits translation coverage
- **Action Required**: No modification needed - reads from i18n.yml

#### `i18n-tools/i18n_3_cleanup.py`
- **Purpose**: Cleans up orphaned translations
- **Action Required**: No modification needed

#### `i18n-tools/i18n_4_generate_prompts.py`
- **Purpose**: Generates LLM prompts for missing translations
- **Action Required**: No modification needed - reads from i18n.yml

#### `i18n-tools/i18n_5_clean_file.py`
- **Purpose**: Cleans language variant files
- **Action Required**: No modification needed

#### `i18n-tools/i18n_workflow.py`
- **Purpose**: Comprehensive i18n workflow management
- **Action Required**: No modification needed

### 5. Translation Guide Files

#### `i18n-tools/translation_guide/`
- **Location**: `/i18n-tools/translation_guide/`
- **Purpose**: Contains translation guidelines and templates
- **Action Required**: 
  - Create new language-specific guide: `{language_code}.md`
  - Copy from `template.md` and customize for the new language

**Example:**
```bash
cp i18n-tools/translation_guide/template.md i18n-tools/translation_guide/ru.md
# Edit ru.md with Russian-specific guidelines
```

### 6. Documentation Files

#### Translation Files Structure
- **Location**: `/docs/` directory
- **Purpose**: Actual translated content
- **Action Required**: Create translated versions of all `.md` files
- **Naming Convention**: `filename.{language_code}.md`

**Example for Russian:**
- `index.md` → `index.ru.md`
- `about/about-us.md` → `about/about-us.ru.md`
- `product/minikvm/index.md` → `product/minikvm/index.ru.md`

## Step-by-Step Process

### 1. Add Language Definition
1. Edit `lang.yml` and add the new language entry with complete `nav_translations`
2. Edit `i18n-tools/i18n.yml` and add the language code to the `languages` list

### 2. Update Frontend JavaScript
1. Edit `docs/assets/javascripts/language-select.js`
2. Add language to `langMap` and `langNames` objects

### 3. Create Translation Guidelines
1. Copy `i18n-tools/translation_guide/template.md` to `i18n-tools/translation_guide/{language_code}.md`
2. Customize the guide for the new language

### 4. Update MkDocs Configuration
1. Run: `python scripts/manage_i18n.py add --languages {language_code}`
2. This automatically updates `mkdocs.yml` with the new language configuration

### 5. Generate Translation Files
1. Run: `python i18n-tools/i18n_workflow.py refresh`
2. This generates prompts for missing translations in `i18n-tools/prompts/`

### 6. Create Translated Content
1. Use the generated prompts to create translated `.md` files
2. Follow the naming convention: `filename.{language_code}.md`

### 7. Test the Setup
1. Run: `python run.py --i18n add`
2. Start MkDocs server: `python run.py`
3. Verify the new language appears in the language selector
4. Test navigation and content display

## File Summary

| File Type | Count | Files |
|-----------|-------|-------|
| **Core Config** | 3 | `lang.yml`, `mkdocs.yml`, `i18n-tools/i18n.yml` |
| **JavaScript** | 1 | `docs/assets/javascripts/language-select.js` |
| **Management Scripts** | 4 | `scripts/manage_i18n.py`, `run.py`, `run-i18n.sh`, `run-en-only.sh` |
| **i18n Tools** | 6 | All scripts in `i18n-tools/` directory |
| **Translation Guides** | 1+ | `i18n-tools/translation_guide/{language_code}.md` |
| **Documentation** | 100+ | All `.md` files in `docs/` directory |

## Important Notes

1. **Never manually edit i18n languages in `mkdocs.yml`** - always use `scripts/manage_i18n.py`

2. **Complete navigation translations required** - All navigation items must be translated in `lang.yml`

3. **File naming convention** - Translation files must follow `filename.{language_code}.md` pattern

4. **Translation workflow** - Use the i18n tools to generate prompts and manage translations systematically

5. **Testing** - Always test the new language setup before deploying

6. **Consistency** - Ensure all navigation items, page titles, and UI elements are consistently translated

## Current Supported Languages

- **en**: English (default)
- **zh**: 简体中文 (Simplified Chinese)
- **ja**: 日本語 (Japanese)
- **ko**: 한국어 (Korean)
- **fr**: Français (French)
- **de**: Deutsch (German)
- **it**: Italiano (Italian)
- **es**: Español (Spanish)
- **pt**: Português (Portuguese)
- **ro**: Română (Romanian)

## Tools and Commands

### Essential Commands
```bash
# Add new language to mkdocs.yml
python scripts/manage_i18n.py add --languages ru

# Remove languages from mkdocs.yml
python scripts/manage_i18n.py remove --languages ru

# List current languages
python scripts/manage_i18n.py list

# Run complete i18n workflow
python i18n-tools/i18n_workflow.py refresh

# Run MkDocs with all languages
python run.py --i18n add

# Run MkDocs with English only
python run.py --i18n remove
```

This guide provides a comprehensive overview of all files and configurations needed to add a new language to the Openterface website project.
