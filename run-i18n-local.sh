#!/bin/sh
# Quick script to add all languages and run MkDocs on local network
# Output is shown on screen and written to a timestamped log file
LOG_DIR="log"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/mkdocs-i18n-local-$(date +%Y-%m-%d-%H%M%S).log"
echo "=== MkDocs i18n (local) started at $(date) ===" | tee "$LOG_FILE"
python openterface-cms/scripts/prepare_build.py --i18n-mode full --action serve --local-network --port 8002 2>&1 | tee -a "$LOG_FILE"

