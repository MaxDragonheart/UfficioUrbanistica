#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start restore"
echo "NOTE: use only in development!!"

# Usermanager
echo "- restore fixtures for Usermanager"
python3 ../project/manage.py loaddata ../project/fixtures/usermanager/userprofile.json

# Standard Apps
echo "- restore fixtures for Django's standard apps"
python3 ../project/manage.py loaddata ../project/fixtures/sites.json
python3 ../project/manage.py loaddata ../project/fixtures/flatpages.json

# Core
echo "- restore fixtures for Core app"
python3 ../project/manage.py loaddata ../project/fixtures/core/sitecustomization.json

# Link
echo "- restore fixtures for Link app"
python3 ../project/manage.py loaddata ../project/fixtures/link/link.json

# Media
echo "- restore fixtures for Media app"
python3 ../project/manage.py loaddata ../project/fixtures/media/fileupload.json

# Sections
echo "- restore fixtures for Sections app"
python3 ../project/manage.py loaddata ../project/fixtures/sections/section.json
python3 ../project/manage.py loaddata ../project/fixtures/sections/sectionpost.json

# Open GeoData
echo "- restore fixtures for Open GeoData app"
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/categories.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/geoserverdomain.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/geoserverworkspace.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/ogclayer.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/webgisproject.json

echo "End process"