#!/usr/bin/env bash

echo "- Make folders for fixtures"
bash ./make_fixtures_folders.sh

echo "- Copy fixtures into project folder"
cd ..
cp -r media-folder/demo_data/fixtures project/

echo "- Restore fixtures"
cd ./scripts/
bash ./local_restore_fixtures.sh