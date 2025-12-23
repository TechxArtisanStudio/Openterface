# Event Management Tool

Automatically generates `docs/event/index.*.md` files for all supported languages using event definitions and translations from `docs/assets/i18n-sites/events.json`.

## Overview

This tool generates multilingual event index pages that list all event sessions with links to their updates pages. Supported languages are loaded from `docs/assets/i18n-sites/lang.yml` (single source of truth) via the `I18nConfig` class.

## Usage

### Generate All Languages (Default)

```bash
python scripts/event-tool/manage_events.py
```

This generates `docs/event/index.md` and `docs/event/index.{lang}.md` files for all languages defined in `lang.yml`.

### Generate Specific Language

```bash
python scripts/event-tool/manage_events.py --language zh
```

This generates only the index file for the specified language.

## Configuration

### events.json Structure

The tool reads event definitions from `docs/assets/i18n-sites/events.json`:

```json
{
  "events": [
    {
      "id": "exhibition",
      "folder": "exhibition",
      "translations": {
        "en": "Exhibition",
        "zh": "展览",
        "ja": "展示会",
        ...
      }
    }
  ],
  "link_text": {
    "en": "Updates & Events",
    "zh": "更新与活动",
    ...
  },
  "page_metadata": {
    "en": {
      "title": "Events",
      "description": "Openterface events, exhibitions, and community activities",
      "keywords": "Openterface events, exhibitions, contests, community activities"
    },
    ...
  }
}
```

### Adding a New Event

1. Add the event folder to `docs/event/` (e.g., `docs/event/my-new-event/`)
2. Create an `updates/` subdirectory (e.g., `docs/event/my-new-event/updates/`)
3. Add event definition to `docs/assets/i18n-sites/events.json`:
   - Add `id`: unique identifier
   - Add `folder`: folder name in `docs/event/`
   - Add `translations`: translations for all languages in `lang.yml`
4. Run the tool to regenerate index files

### Adding Translations

When adding a new language to `lang.yml`:

1. Update `lang.yml` with the new language
2. Add translations for all events in `events.json`
3. Add `link_text` translation
4. Add `page_metadata` translation
5. Run the tool to generate index files for the new language

## Generated Files

The tool generates:
- `docs/event/index.md` (default language, usually English)
- `docs/event/index.{lang}.md` (one file per additional language)

Each file contains:
- Frontmatter with SEO metadata (title, description, keywords)
- H1 heading with translated "Events" title
- H2 sections for each event with translated event name
- Links to each event's updates page

## Integration

The tool is integrated into the build workflow via `scripts/prepare_build.py` and runs automatically during:
- Full i18n builds
- CI/CD builds

## Validation

The tool performs several validations:

1. **Language Validation**: Checks that `events.json` has translations for all languages in `lang.yml` (warns if missing, falls back to English)
2. **Folder Validation**: Verifies that event folders exist in `docs/event/` before generating links
3. **Updates Directory**: Checks if `updates/` subdirectory exists (warns if missing)

## Dependencies

- `scripts/i18n-shared/lang_loader.py`: Loads supported languages from `lang.yml`
- `docs/assets/i18n-sites/events.json`: Event definitions and translations
- `docs/assets/i18n-sites/lang.yml`: Single source of truth for supported languages

## Examples

### Example: Adding a New Event

1. Create event directory:
   ```bash
   mkdir -p docs/event/hackathon-2025/updates
   ```

2. Add to `events.json`:
   ```json
   {
     "id": "hackathon-2025",
     "folder": "hackathon-2025",
     "translations": {
       "en": "Hackathon 2025",
       "zh": "黑客马拉松 2025",
       ...
     }
   }
   ```

3. Run the tool:
   ```bash
   python scripts/event-tool/manage_events.py
   ```

4. The new event will appear in all generated `docs/event/index.*.md` files.

## Troubleshooting

### Missing Translations Warning

If you see warnings about missing translations:
- Add the missing translations to `events.json`
- The tool will fallback to English for missing languages

### Event Folder Not Found

If an event folder is missing:
- Create the folder in `docs/event/`
- Ensure it has an `updates/` subdirectory
- Re-run the tool

### Language Not in lang.yml

If a language appears in `events.json` but not in `lang.yml`:
- The tool will show an info message
- The language will be ignored (only languages in `lang.yml` are processed)

