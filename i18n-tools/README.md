## i18n workflow for docs

Use the tools in `i18n-tools/` in this sequence.

### 1) Generate i18n config from lang.yml

Creates `i18n-tools/i18n.yml` with `default_language` and ordered `languages` from `lang.yml`.

```bash
python3 i18n-tools/i18n_1_from_mkdocs.py --lang lang.yml --mkdocs mkdocs.yml --output i18n-tools/i18n.yml

# overwrite if it exists
python3 i18n-tools/i18n_1_from_mkdocs.py --lang lang.yml --mkdocs mkdocs.yml --output i18n-tools/i18n.yml --force
```

### 2) Audit translation coverage

Produces `i18n_audit.csv` at repo root. Cells: 1=present, 0=missing.

```bash
python3 i18n-tools/i18n_2_audit.py --docs docs --config i18n-tools/i18n.yml --output i18n_audit.csv

# only rows with missing translations
python3 i18n-tools/i18n_2_audit.py --docs docs --config i18n-tools/i18n.yml --only-missing

# fail CI if any missing
python3 i18n-tools/i18n_2_audit.py --docs docs --config i18n-tools/i18n.yml --fail-on-missing
```

### 3) Cleanup orphaned translations (no English base)

Lists groups where English base is missing but translations exist; lets you delete them. After deletions, auto-refreshes `i18n_audit.csv`.

```bash
# preview only (no deletion)
python3 i18n-tools/i18n_3_cleanup.py --docs docs --config i18n-tools/i18n.yml --dry-run

# delete all candidates without prompts (use with caution)
python3 i18n-tools/i18n_3_cleanup.py --docs docs --config i18n-tools/i18n.yml --yes-all

# interactive (confirm all, or one-by-one)
python3 i18n-tools/i18n_3_cleanup.py --docs docs --config i18n-tools/i18n.yml
```

### 4) Generate LLM prompts for missing translations

Creates Markdown task files in `i18n-tools/prompts/` for every English page missing one or more translations.

**Basic usage:**

```bash
python3 i18n-tools/i18n_4_generate_prompts.py --docs docs --config i18n-tools/i18n.yml --output-dir i18n-tools/prompts --overwrite
```

**With custom translation guide directory:**

```bash
python3 i18n-tools/i18n_4_generate_prompts.py --docs docs --translation-guide-dir i18n-tools/translation_guide --overwrite
```

**Note:** HTML files are no longer supported as all HTML templates have been unified with Jinja2 conditionals.

**Details:**

- Filenames are flattened: `docs/app/android/index.md` -> `i18n-tools/prompts/app_android_index.llm-task.md`
- Each prompt includes:
  - A coverage line: `group,en,zh,ja,ko,fr,de,it,es,pt,ro` (1/0)
  - Missing targets prefixed with `docs/` (e.g., `docs/app/android/index.zh.md`)
  - **Translation guidelines** (global + language-specific)
  - The English source path (e.g., `docs/app/android/index.md`) followed by a fenced code block of its contents

### 5) Clean language variants for files or directories

Removes all language variant files for English markdown files while keeping the original English files. Can process a single file or recursively scan a directory and all its subdirectories.

**Basic usage (single file):**

```bash
python3 i18n-tools/i18n_5_clean_file.py /path/to/file.md
```

**Process entire directory recursively:**

```bash
python3 i18n-tools/i18n_5_clean_file.py /path/to/directory
```

**Delete all files including the base English files:**

```bash
python3 i18n-tools/i18n_5_clean_file.py /path/to/file.md --include-base
python3 i18n-tools/i18n_5_clean_file.py /path/to/directory --include-base
```

**Skip confirmation prompts:**

```bash
python3 i18n-tools/i18n_5_clean_file.py /path/to/file.md --yes
python3 i18n-tools/i18n_5_clean_file.py /path/to/directory --yes
```

**Preview what would be deleted (dry run):**

```bash
python3 i18n-tools/i18n_5_clean_file.py /path/to/file.md --dry-run
python3 i18n-tools/i18n_5_clean_file.py /path/to/directory --dry-run
```

**Examples:**

```bash
# Clean all language variants of specifications.md (keep specifications.md)
python3 i18n-tools/i18n_5_clean_file.py docs/product/minikvm/specifications.md

# Clean all language variants in the entire minikvm directory
python3 i18n-tools/i18n_5_clean_file.py docs/product/minikvm/

# Delete everything including the base English files in a directory
python3 i18n-tools/i18n_5_clean_file.py docs/product/minikvm/ --include-base --yes

# Preview what would be deleted in a directory
python3 i18n-tools/i18n_5_clean_file.py docs/product/minikvm/ --dry-run
```

### 6) Translation Guide System

The system automatically loads translation guides from `i18n-tools/translation_guide/` to ensure consistent, high-quality translations.

**Guide Structure:**

- `global.md` - Universal translation standards for all languages
- `{language}.md` - Language-specific guidelines (e.g., `es.md`, `zh.md`)
- `template.md` - Template for creating new language guides

**Creating Language-Specific Guides:**

```bash
# Copy template for new language
cp i18n-tools/translation_guide/template.md i18n-tools/translation_guide/zh.md

# Customize the guide for Chinese-specific needs
# Edit i18n-tools/translation_guide/zh.md
```

**Guide Features:**

- **Hierarchical loading** - Global guide loads first, then language-specific guides
- **Automatic integration** - Guides are embedded in generated prompts
- **Fallback support** - Works even if guides are missing
- **Version control** - Track changes and updates to guidelines

**Translation Quality Benefits:**

- Consistent terminology across all languages
- Brand consistency for Openterface terminology
- Cultural adaptations for each target language
- Technical accuracy for specialized terms
- Quality checklists and best practices

### Notes

- Language precedence in scripts: `--languages` > `--config` YAML > `lang.yml` > `mkdocs.yml` > defaults
- The script now reads languages from `lang.yml` instead of `mkdocs.yml` i18n plugin configuration
- Default language is determined from `theme.language` in `mkdocs.yml` or falls back to 'en'
- Only languages with `build: true` (or no build field) are included from `lang.yml`
- Audit/cleanup scan only `.md` files (HTML templates are now unified with Jinja2 conditionals)
- Translation guides are automatically loaded from `i18n-tools/translation_guide/`
- Consider adding `i18n_audit.csv` to `.gitignore` if you don't want to commit it
- For detailed guide system documentation, see `i18n-tools/translation_guide/README.md`
