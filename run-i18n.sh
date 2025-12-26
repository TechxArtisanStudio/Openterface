#!/bin/bash
# Quick script to add all languages and run MkDocs

echo "Adding all languages and starting MkDocs server..."
python openterface-cms/scripts/prepare_build.py --i18n-mode full --action serve
