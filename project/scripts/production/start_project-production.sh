#!/usr/bin/env bash
echo "START UfficioUrbanistica"

echo "--- Make migrations and collect static files"
bash ./migrate-collectstic.sh

echo "--- Copy startup fixtures into project folder"
cp -r media-folder/demo_data/fixtures project/

echo "--- Upload startup fixtures into DB"
bash ./backup_restore/restore-fixtures.sh