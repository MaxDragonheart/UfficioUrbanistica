#!/usr/bin/env bash
echo "START UfficioUrbanistica in STAGING"

echo "--- Make migrations and collect static files"
bash ./migrate-collecstatic.sh

echo "--- Copy startup fixtures into project folder"
cp -r media-folder/demo_data/fixtures project/

echo "--- Upload startup fixtures into DB"
bash ./restore-fixtures.sh