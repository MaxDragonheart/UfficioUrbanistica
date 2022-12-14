#!/usr/bin/env bash
echo "- Creation of fixtures folders"

echo "1. Move into parent folder"
cd ..
pwd
echo "2. Create fixtures folders"
mkdir -p project/fixtures/link project/fixtures/media project/fixtures/sections project/fixtures/usermanager project/fixtures/core project/fixtures/opengeodata

echo "Folders created!"