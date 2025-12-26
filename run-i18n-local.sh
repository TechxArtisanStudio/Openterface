#!/bin/bash
# Quick script to add all languages and run MkDocs on local network

echo "Adding all languages and starting MkDocs server on local network..."
python openterface-cms/scripts/prepare_build.py --i18n-mode full --action serve --local-network --port 8002

