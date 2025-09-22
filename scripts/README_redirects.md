# Dynamic Redirect System

## Overview

This project uses a dynamic redirect system that automatically generates language-specific redirects based on the `mkdocs.yml` configuration. This eliminates the need to manually maintain redirect mappings for each language.

## How It Works

1. **Source Configuration**: Redirects are defined once in `mkdocs.yml` under the `redirects` plugin
2. **Dynamic Generation**: The `404.html` page automatically generates language variants for all supported languages
3. **Automatic Sync**: The `sync_redirects.py` script keeps the 404.html redirects in sync with mkdocs.yml

## Supported Redirect Types

### Internal Redirects
```yaml
app.md: app/overview.md
```
Automatically generates:
- `/app` → `/app/overview/`
- `/zh/app` → `/zh/app/overview/`
- `/fr/app` → `/fr/app/overview/`
- ... (for all supported languages)

### External Redirects
```yaml
buy-mini-kvm.md: https://www.crowdsupply.com/techxartisan/openterface-mini-kvm
```
Automatically generates:
- `/buy-mini-kvm` → `https://www.crowdsupply.com/techxartisan/openterface-mini-kvm`
- `/zh/buy-mini-kvm` → `https://www.crowdsupply.com/techxartisan/openterface-mini-kvm`
- `/fr/buy-mini-kvm` → `https://www.crowdsupply.com/techxartisan/openterface-mini-kvm`
- ... (same external URL for all languages)

## Usage

### Adding New Redirects
1. Add the redirect to `mkdocs.yml` under `redirects.redirect_maps:`
2. Run the sync script: `python scripts/sync_redirects.py`
3. The 404.html will automatically include the new redirect for all languages

### Supported Languages
Languages are automatically read from `lang.yml`:
- zh (简体中文)
- ja (日本語)
- ko (한국어)
- fr (Français)
- de (Deutsch)
- it (Italiano)
- es (Español)
- pt (Português)
- ro (Română)

## Files

- `mkdocs.yml` - Source redirect configuration
- `lang.yml` - Supported languages list
- `docs/overrides/404.html` - Dynamic redirect implementation
- `scripts/sync_redirects.py` - Sync script

## Benefits

1. **Single Source of Truth**: Redirects defined once in mkdocs.yml
2. **Automatic Language Support**: All redirects automatically work in all languages
3. **Easy Maintenance**: Add redirects once, works everywhere
4. **Static Site Compatible**: Pure client-side JavaScript, works on GitHub Pages
5. **No Plugin Conflicts**: Bypasses mkdocs-redirects plugin compatibility issues
