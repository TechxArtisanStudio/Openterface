#!/bin/bash
# Quick script to remove all languages except English and run MkDocs

echo "Removing all languages except English and starting MkDocs server..."
python openterface-cms/scripts/prepare_build.py --i18n-mode en-only --action serve
