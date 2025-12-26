# Migration Summary: Decouple Tools to CMS Submodule

## What Changed

### Removed from Public Repo
- ❌ `scripts/` directory (moved to private `openterface-cms` submodule)
- ❌ Tool dependencies from `requirements.txt`

### Added to Public Repo
- ✅ `openterface-cms/` submodule (private repository)
- ✅ `.gitmodules` configuration
- ✅ Updated GitHub Actions workflow

### Kept in Public Repo
- ✅ `docs/assets/i18n-sites/` - i18n translation assets (content/data)
- ✅ All documentation markdown files
- ✅ `mkdocs.yml` configuration

## New Workflow

### Local Development

```bash
# Clone with submodule
git clone --recursive https://github.com/TechxArtisanStudio/Openterface.git

# Or initialize submodule if already cloned
git submodule update --init --recursive

# Install CMS dependencies
pip install -r openterface-cms/requirements.txt

# Run build
python openterface-cms/scripts/prepare_build.py --i18n-mode en-only --action serve
```

### Updating CMS Tools

```bash
# Make changes in CMS submodule
cd openterface-cms
# ... make changes ...
git add .
git commit -m "Update CMS tools"
git push

# Update submodule reference in main repo
cd ..
git add openterface-cms
git commit -m "Update openterface-cms submodule"
git push
```

## Repository Structure

```
Openterface/ (public)
├── docs/                    # Documentation content
│   └── assets/
│       └── i18n-sites/      # i18n assets (public)
├── openterface-cms/         # Git submodule (private)
│   ├── scripts/             # Build tools
│   ├── templates/          # HTML templates
│   └── data/               # Data adapter layer
├── .gitmodules             # Submodule config
└── mkdocs.yml              # MkDocs config
```

## Benefits

1. **Privacy**: Build tools and processes are private
2. **Clean Separation**: Docs repo only contains content
3. **Future-Ready**: Structure supports web frontend and database
4. **Maintainable**: Clear organization

## Files Modified

- `.gitmodules` - Added submodule configuration
- `.github/workflows/build-mkdocs.yml` - Updated to use CMS submodule
- `requirements.txt` - Removed tool dependencies, added note
- `README.md` - Added development setup instructions

## Files Removed

- `scripts/` - Entire directory moved to CMS submodule

