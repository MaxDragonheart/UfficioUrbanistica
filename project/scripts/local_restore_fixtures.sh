#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start backup"
echo "NOTE: use only in development!!"

# Usermanager
echo "- make fixtures for Usermanager"
python3 ../project/manage.py loaddata ../project/fixtures/usermanager/userprofile.json

# Standard Apps
echo "- make fixtures for Django's standard apps"
python3 ../project/manage.py loaddata ../project/fixtures/sites.json
python3 ../project/manage.py loaddata ../project/fixtures/flatpages.json

# Link
echo "- make fixtures for Link app"
python3 ../project/manage.py loaddata ../project/fixtures/link/link.json

# Media
echo "- make fixtures for Media app"
python3 ../project/manage.py loaddata ../project/fixtures/media/fileupload.json

# Sections
echo "- make fixtures for Sections app"
python3 ../project/manage.py loaddata ../project/fixtures/sections/section.json
python3 ../project/manage.py loaddata ../project/fixtures/sections/sectionpost.json

echo "End process"