#!/bin/bash
# Quick script to remove all languages except English and run MkDocs on local network

echo "Removing all languages except English and starting MkDocs server on local network..."
python scripts/prepare_build.py --i18n-mode en-only --action serve --local-network --port 8002

