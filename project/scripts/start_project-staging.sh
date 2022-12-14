#!/usr/bin/env bash
echo "START UfficioUrbanistica in STAGING"

echo "--- Make migrations and collect static files"
bash ./migrate-collectstic.sh

echo "--- Make folders for startup fixtures"
bash ./make-fixtures-folders.sh

echo "--- Copy startup fixtures into project folder"
cd ..
cp -r media-folder/demo_data/fixtures project/

echo "--- Upload startup fixtures into DB"
cd ./scripts/
bash ./local_restore-fixtures.sh