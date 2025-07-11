#!/bin/bash

# Ensure script is run from the parent directory of Openterface
target_dir="Openterface"

# Check if the target directory exists
if [ ! -d "$target_dir" ]; then
    echo "Error: '$target_dir' directory not found. Please run this script from its parent directory."
    exit 1
fi

# List of repositories to clone
repos=(
    "git@github.com:TechxArtisanStudio/Openterface_zh.git"
    "git@github.com:TechxArtisanStudio/Openterface_es.git"
    "git@github.com:TechxArtisanStudio/Openterface_fr.git"
    "git@github.com:TechxArtisanStudio/Openterface_it.git"
    "git@github.com:TechxArtisanStudio/Openterface_ko.git"
    "git@github.com:TechxArtisanStudio/Openterface_pt.git"
    "git@github.com:TechxArtisanStudio/Openterface_ro.git"
)

# Clone each repository into the Openterface/ directory
for repo in "${repos[@]}"; do
    echo "Cloning $repo into $target_dir/ ..."
    git -C "$target_dir" clone "$repo"
done

echo "All repositories cloned into '$target_dir/'."

# chmod +x clone_repos.sh
# cd ..
# ./openterface/clone_repos.sh

for d in ~/project/openterface/website/Openterface_*; do
  echo "source ../.venv/bin/activate" > "$d/.envrc"
  direnv allow "$d"
done