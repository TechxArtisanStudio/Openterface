#!/bin/bash
# Quick script to remove all languages except English and run MkDocs on local network

echo "Removing all languages except English and starting MkDocs server on local network..."
python run.py --i18n remove --local-network --port 8002

