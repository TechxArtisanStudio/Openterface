#!/bin/sh
# Quick script to remove all languages except English and run MkDocs
# Output is shown on screen and written to a timestamped log file
LOG_DIR="log"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/mkdocs-en-only-$(date +%Y-%m-%d-%H%M%S).log"
echo "=== MkDocs en-only started at $(date) ===" | tee "$LOG_FILE"
python openterface-cms/scripts/prepare_build.py --i18n-mode en-only --action serve 2>&1 | tee -a "$LOG_FILE"
