#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start backup"
echo "NOTE: use only in development!!"

# Usermanager
echo "- make fixtures for Usermanager"
python3 ../project/manage.py loaddata ../project/fixtures/usermanager_userprofile.json

# Standard Apps
echo "- make fixtures for Django's standard apps"
python3 ../project/manage.py loaddata ../project/fixtures/sites.json
python3 ../project/manage.py loaddata ../project/fixtures/flatpages.json

# Link
python3 ../project/manage.py loaddata ../project/fixtures/link/link.json

# Media
python3 ../project/manage.py loaddata ../project/fixtures/media/fileupload.json

# Sections
python3 ../project/manage.py loaddata ../project/fixtures/sections/section.json
python3 ../project/manage.py loaddata ../project/fixtures/sections/sectionpost.json

echo "End process"