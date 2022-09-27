#!/usr/bin/env bash
echo "Creation of fixtures folders..."

echo "# Move into parent folder"
cd ..
pwd
echo "# Create fixtures folders"
mkdir -p project/fixtures/link project/fixtures/media project/fixtures/sections project/fixtures/usermanager project/fixtures/core project/fixtures/opengeodata

echo "Folders created!"