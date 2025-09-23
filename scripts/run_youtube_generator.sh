#!/bin/bash

# YouTube Reviews Generator Wrapper Script
# This script sets up the proxy environment and runs the YouTube generator

# Set proxy configuration
export http_proxy=http://127.0.0.1:1087
export https_proxy=http://127.0.0.1:1087

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the Python script with all passed arguments
python "$SCRIPT_DIR/generate_youtube_reviews.py" "$@"
