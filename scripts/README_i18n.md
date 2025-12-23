# Internationalization (i18n) Management

## Overview

This project uses a **separated i18n configuration system** for better management of multi-language support.

## File Structure

- **`docs/assets/i18n-sites/lang.yml`** - Contains all language translations and configurations (single source of truth)
- **`mkdocs.yml`** - Contains the active language configuration (managed by scripts)
- **`scripts/manage_i18n.py`** - Script to manage language configurations

## Important Rules

### ⚠️ DO NOT manually edit i18n translations in `mkdocs.yml`

The i18n translations should **ONLY** be managed through the `lang.yml` file and the management script. This prevents:

- Duplication of translations
- Inconsistencies between files
- Maintenance issues
- Accidental overwrites

### ✅ Correct Workflow

1. **Add new languages**: Edit `docs/assets/i18n-sites/lang.yml` with new language configurations
2. **Apply changes**: Run `python scripts/manage_i18n.py add` to update `mkdocs.yml`
3. **Remove languages**: Run `python scripts/manage_i18n.py remove [language_codes]`
4. **Check status**: Run `python scripts/manage_i18n.py list` to see current configuration

## Script Usage

```bash
# Add all languages from docs/assets/i18n-sites/lang.yml to mkdocs.yml
python scripts/manage_i18n.py add

# Add specific languages only
python scripts/manage_i18n.py add --languages zh ja ko

# Remove all languages except English
python scripts/manage_i18n.py remove

# Remove specific languages
python scripts/manage_i18n.py remove --languages zh ja

# List current language configuration
python scripts/manage_i18n.py list
```

## For AI Agents

When working with this project's i18n system:

1. **NEVER** manually add nav_translations to `mkdocs.yml`
2. **ALWAYS** edit language configurations in `docs/assets/i18n-sites/lang.yml`
3. **ALWAYS** use `scripts/manage_i18n.py` to apply changes to `mkdocs.yml`
4. **UNDERSTAND** that `mkdocs.yml` i18n config is managed, not manually edited

This separation ensures clean, maintainable, and consistent multi-language support.
