#!/bin/bash

# List of repositories to clone
repos=(
    "git@github.com:TechxArtisanStudio/Openterface_jp.git"
    "git@github.com:TechxArtisanStudio/Openterface_zh.git"
    "git@github.com:TechxArtisanStudio/Openterface_es.git"
    "git@github.com:TechxArtisanStudio/Openterface_fr.git"
    "git@github.com:TechxArtisanStudio/Openterface_it.git"
    "git@github.com:TechxArtisanStudio/Openterface_ko.git"
    "git@github.com:TechxArtisanStudio/Openterface_pt.git"
    "git@github.com:TechxArtisanStudio/Openterface_ro.git"
)

# Clone each repository
for repo in "${repos[@]}"; do
    echo "Cloning $repo ..."
    git clone "$repo"
done

echo "All repositories cloned."

# chmod +x clone_openterface_repos.sh
# ./clone_openterface_repos.sh