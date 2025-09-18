#!/bin/bash
# Quick script to remove all languages except English and run MkDocs

echo "Removing all languages except English and starting MkDocs server..."
python run.py --i18n remove
