# Scripts Directory

This directory contains utility scripts for managing the MkDocs documentation site.

## update_config.py

Updates `mkdocs.yml` with dynamic values like package versions and copyright year.

### Usage

```bash
# Update with all dynamic values (fetches versions from APIs)
python scripts/update_config.py

# Update only copyright year (skip API calls for faster local testing)
python scripts/update_config.py --skip-versions

# Update with specific values
python scripts/update_config.py --qt-version v2.1.0 --copyright-year 2025

# Dry run (show what would be updated without making changes)
python scripts/update_config.py --dry-run

# Use a different mkdocs.yml file
python scripts/update_config.py --mkdocs-path custom-mkdocs.yml
```

### Options

- `--mkdocs-path`: Path to mkdocs.yml file (default: mkdocs.yml)
- `--qt-version`: QT version to set (if not provided, will fetch from API)
- `--android-version`: Android version to set (if not provided, will fetch from API)
- `--macos-version`: macOS version to set (if not provided, will fetch from API)
- `--copyright-year`: Copyright year to set (if not provided, will use current year)
- `--skip-versions`: Skip fetching versions from APIs (useful for local testing)
- `--dry-run`: Show what would be updated without making changes

### Integration

This script is used by:
- **GitHub Actions**: Automatically updates config during deployment
- **Local Development**: Called automatically by `run.py` (can be disabled with `--no-update-config`)

## Integration with run.py

The main `run.py` script updates the config by default before serving:

```bash
# Run with config update (current year only, fast) - DEFAULT BEHAVIOR
python run.py

# Run with config update and latest versions (slower, fetches from APIs)
python run.py --fetch-versions

# Run without config update (uses existing config)
python run.py --no-update-config

# Custom port and host
python run.py --port 8080 --host localhost

# Skip config update with custom port
python run.py --no-update-config --port 8080
```
