# Multi-Language Management for MkDocs

This project includes tools to manage multi-language configurations in MkDocs, allowing you to build with or without multiple languages for faster development.

## Quick Start

### Development Mode (English Only)

For faster development when editing English content:

```bash
# Using bash script (recommended)
bash run-en-only.sh

# Or using Python directly
python run.py --i18n remove
```

### Full Multi-Language Build

To build with all languages:

```bash
# Using bash script (recommended)
bash run-i18n.sh

# Or using Python directly
python run.py --i18n add
```

### Specific Languages Only

To build with specific languages:

```bash
python run.py --i18n add --lang zh ja ko
```

### List Current Languages

To see what languages are currently configured:

```bash
# Using bash script (recommended)
bash list-langs.sh

# Or using Python directly
python run.py --i18n list
```

## Bash Scripts

For convenience, several bash scripts are provided:

- `run-i18n.sh` - Add all languages and start MkDocs server
- `run-en-only.sh` - Remove all languages except English and start MkDocs server
- `list-langs.sh` - List current language configuration

## Script Usage

The `scripts/manage_i18n.py` script can be used directly:

```bash
# Add all languages from lang.yml
python scripts/manage_i18n.py add

# Add specific languages
python scripts/manage_i18n.py add --languages zh ja ko

# Remove all languages except English
python scripts/manage_i18n.py remove

# Remove specific languages
python scripts/manage_i18n.py remove --languages zh ja

# List current languages
python scripts/manage_i18n.py list
```

## GitHub Actions

The GitHub Actions workflow automatically adds all languages before building, ensuring the production site always includes all translations.

## File Structure

- `mkdocs.yml` - Main MkDocs configuration (starts with English only)
- `lang.yml` - Contains all language configurations and translations
- `scripts/manage_i18n.py` - Script to manage i18n configuration
- `run.py` - Enhanced run script with i18n management flags

## Workflow

1. **Development**: Use `--i18n remove` for faster builds when editing English content
2. **Testing**: Use `--i18n add` to test with all languages
3. **Production**: GitHub Actions automatically builds with all languages
4. **Specific Testing**: Use `--lang` to test specific language combinations
