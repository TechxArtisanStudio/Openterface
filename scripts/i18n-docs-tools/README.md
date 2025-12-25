## i18n workflow for docs

Use the tools in `scripts/i18n-docs-tools/` in this sequence.

**Note:** All tools read directly from `docs/assets/i18n-sites/lang.yml` as the single source of truth.
No intermediate config generation step is needed.

### 1) Audit translation coverage

Produces `i18n_audit.csv` at repo root. Cells: 1=present, 0=missing.

```bash
python3 scripts/i18n-docs-tools/audit_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml --output scripts/i18n-docs-tools/i18n_audit.csv

# only rows with missing translations
python3 scripts/i18n-docs-tools/audit_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml --only-missing

# fail CI if any missing
python3 scripts/i18n-docs-tools/audit_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml --fail-on-missing
```

### 3) Cleanup orphaned translations (no English base)

Lists groups where English base is missing but translations exist; lets you delete them. After deletions, auto-refreshes `i18n_audit.csv`.

```bash
# preview only (no deletion)
python3 scripts/i18n-docs-tools/cleanup_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml --dry-run

# delete all candidates without prompts (use with caution)
python3 scripts/i18n-docs-tools/cleanup_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml --yes-all

# interactive (confirm all, or one-by-one)
python3 scripts/i18n-docs-tools/cleanup_translations.py --docs docs --config docs/assets/i18n-sites/lang.yml
```

### 4) Generate LLM prompts for missing translations

Creates Markdown task files in `scripts/i18n-docs-tools/prompts/` for every English page missing one or more translations.

**Basic usage:**

```bash
python3 scripts/i18n-docs-tools/generate_prompts.py --docs docs --config docs/assets/i18n-sites/lang.yml --output-dir scripts/i18n-docs-tools/prompts --overwrite
```

**With custom translation guide directory:**

```bash
python3 scripts/i18n-docs-tools/generate_prompts.py --docs docs --translation-guide-dir scripts/i18n-docs-tools/translation_guide --overwrite
```

**Note:** HTML files are no longer supported as all HTML templates have been unified with Jinja2 conditionals.

**Details:**

- Filenames are flattened: `docs/app/android/index.md` -> `scripts/i18n-docs-tools/prompts/app_android_index.llm-task.md`
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
python3 scripts/i18n-docs-tools/clean_file_variants.py docs/product/minikvm/specifications.md

# Clean all language variants in the entire minikvm directory
python3 scripts/i18n-docs-tools/clean_file_variants.py docs/product/minikvm/

# Delete everything including the base English files in a directory
python3 scripts/i18n-docs-tools/clean_file_variants.py docs/product/minikvm/ --include-base --yes

# Preview what would be deleted in a directory
python3 scripts/i18n-docs-tools/clean_file_variants.py docs/product/minikvm/ --dry-run
```

### 6) Translate with LLM APIs

Automatically translate English markdown files to target languages using local or cloud LLM APIs.

**Supported Providers:**
- **LM Studio** (local, default) - Free local translation using your own models
- **OpenAI** - GPT-4, GPT-3.5, and other OpenAI models
- **Anthropic** - Claude 3 models (Opus, Sonnet, Haiku)

**Basic usage:**

```bash
# Translate to all missing languages using LM Studio (local)
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md

# Translate to specific languages
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --langs zh,ja,ko

# Overwrite existing translations
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --overwrite
```

**Using OpenAI:**

```bash
# Set API key (recommended: use environment variable)
export OPENAI_API_KEY=sk-...

# Translate with GPT-4
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --provider openai --model gpt-4-turbo-preview

# Translate with GPT-3.5 (faster, cheaper)
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --provider openai --model gpt-3.5-turbo
```

**Using Anthropic Claude:**

```bash
# Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# Translate with Claude Opus
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --provider anthropic --model claude-3-opus-20240229

# Translate with Claude Sonnet (faster, cheaper)
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --provider anthropic --model claude-3-sonnet-20240229
```

**Advanced options:**

```bash
# Custom temperature (lower = more consistent, higher = more creative)
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --temperature 0.2

# Custom API endpoint
export LM_STUDIO_API_URL=http://localhost:1234/v1
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --provider lmstudio

# Dry run (preview without translating)
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --dry-run

# Configuration file
python3 scripts/i18n-docs-tools/translate_with_llm.py docs/product/kvm-go/updates/article.md --config-file .translation_config.yml
```

**Configuration file example (.translation_config.yml):**

```yaml
provider: openai
api_key: ${OPENAI_API_KEY}  # Can use env var references
api_url: https://api.openai.com/v1
model: gpt-4-turbo-preview
temperature: 0.3
default_languages: [zh, ja, ko, fr, de, it, es, pt, ro]
```

**Features:**
- Automatically loads translation guides (global + language-specific)
- Preserves markdown formatting, links, code blocks, and frontmatter
- Skips existing translations by default (use `--overwrite` to replace)
- Supports multiple API providers with easy switching
- Handles errors gracefully with clear messages
- Integrates with existing i18n workflow

**Note:** The script automatically uses translation guides from `scripts/i18n-docs-tools/translation_guide/` to ensure consistent, high-quality translations.

### 7) Translation Guide System

The system automatically loads translation guides from `scripts/i18n-docs-tools/translation_guide/` to ensure consistent, high-quality translations.

**Guide Structure:**

- `global.md` - Universal translation standards for all languages
- `{language}.md` - Language-specific guidelines (e.g., `es.md`, `zh.md`)
- `template.md` - Template for creating new language guides

**Creating Language-Specific Guides:**

```bash
# Copy template for new language
cp scripts/i18n-docs-tools/translation_guide/template.md scripts/i18n-docs-tools/translation_guide/zh.md

# Customize the guide for Chinese-specific needs
# Edit scripts/i18n-docs-tools/translation_guide/zh.md
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
- Translation guides are automatically loaded from `scripts/i18n-docs-tools/translation_guide/`
- Consider adding `i18n_audit.csv` to `.gitignore` if you don't want to commit it
- For detailed guide system documentation, see `scripts/i18n-docs-tools/translation_guide/README.md`
- The i18n config is now consolidated at `docs/assets/i18n-sites/lang.yml` (single source of truth)
