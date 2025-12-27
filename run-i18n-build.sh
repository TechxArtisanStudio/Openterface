#!/bin/bash
# Quick script to build site/ with all languages

echo "Building site with all languages..."
python openterface-cms/scripts/prepare_build.py --i18n-mode full --action build

