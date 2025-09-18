# i18n Workflow Script

A comprehensive command-line tool for managing i18n workflows in MkDocs projects. This script replaces the Jupyter notebook (`i18n_workflow.ipynb`) with a single executable command.

## Features

- **Generate i18n config** from mkdocs.yml
- **Audit translation coverage** across all languages
- **Generate LLM prompts** for missing translations
- **Display detailed coverage reports**
- **Quick refresh** of entire workflow
- **Automatic virtual environment detection**

## Installation

No installation required! The script automatically detects and uses your project's virtual environment.

## Usage

```bash
# Run complete workflow refresh (default - no arguments needed!)
python i18n_workflow.py

# Show current status
python i18n_workflow.py status

# Generate i18n config from mkdocs.yml
python i18n_workflow.py config --force

# Run translation coverage audit
python i18n_workflow.py audit

# Generate LLM prompts for missing translations
python i18n_workflow.py prompts --overwrite

# Show detailed coverage report
python i18n_workflow.py report

# Show available translation guides
python i18n_workflow.py guides
```

## Commands

| Command | Description |
|---------|-------------|
| `refresh` | Run complete workflow refresh (config + audit + prompts + report) **[DEFAULT]** |
| `status` | Show current status and available actions |
| `config` | Generate i18n.yml from mkdocs.yml |
| `audit` | Run translation coverage audit |
| `prompts` | Generate LLM prompts for missing translations |
| `report` | Show detailed coverage report |
| `guides` | Show available translation guides |

## Options

| Option | Description |
|--------|-------------|
| `--project-root` | Project root directory (default: current directory) |
| `--force` | Force overwrite existing files |
| `--overwrite` | Overwrite existing prompt files |
| `--only-missing` | Show only files with missing translations |
| `--fail-on-missing` | Exit with error code if missing translations found |

## Examples

```bash
# Quick start - run everything (no arguments needed!)
python i18n_workflow.py

# Check status without running anything
python i18n_workflow.py status

# Generate only prompts
python i18n_workflow.py prompts --overwrite

# Show only missing translations
python i18n_workflow.py report --only-missing

# Run audit and fail if missing translations found
python i18n_workflow.py audit --fail-on-missing
```

## Output

The script provides:
- ✅/❌ Status indicators for each step
- 📊 Coverage summary with percentages
- 📋 Detailed list of missing translations
- 📝 Files that need to be created
- 📚 Available translation guides
- 🤖 Generated prompt files

## Virtual Environment

The script automatically detects and uses your project's virtual environment in this order:
1. `.venv/bin/python`
2. `venv/bin/python`
3. `~/.virtualenvs/{project-name}/bin/python`
4. System Python (fallback)

## Requirements

- Python 3.6+
- PyYAML (automatically detected if in virtual environment)
- MkDocs project with i18n configuration

## Migration from Jupyter Notebook

This script replaces the `i18n_workflow.ipynb` notebook. All functionality is preserved:

- ✅ Generate i18n config
- ✅ Audit translation coverage  
- ✅ Generate LLM prompts
- ✅ Show coverage reports
- ✅ Quick actions and status

Simply run `python i18n_workflow.py refresh` instead of executing notebook cells.
