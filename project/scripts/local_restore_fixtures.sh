#!/usr/bin/env bash
# Useful only in development on local machine.
echo "- Start restore"
echo "NOTE: use this process only in development!!"

# Usermanager
echo "1. Restore fixtures for Usermanager"
python3 ../project/manage.py loaddata ../project/fixtures/usermanager/userprofile.json

# Standard Apps
echo "2. Restore fixtures for Django's standard apps"
python3 ../project/manage.py loaddata ../project/fixtures/sites.json
python3 ../project/manage.py loaddata ../project/fixtures/flatpages.json

# Core
echo "3. Restore fixtures for Core app"
python3 ../project/manage.py loaddata ../project/fixtures/core/sitecustomization.json

# Link
echo "4. Restore fixtures for Link app"
python3 ../project/manage.py loaddata ../project/fixtures/link/link.json

# Media
echo "5. Restore fixtures for Media app"
python3 ../project/manage.py loaddata ../project/fixtures/media/fileupload.json

# Sections
echo "6. Restore fixtures for Sections app"
python3 ../project/manage.py loaddata ../project/fixtures/sections/section.json
python3 ../project/manage.py loaddata ../project/fixtures/sections/sectionpost.json

# Open GeoData
echo "7. Restore fixtures for Open GeoData app"
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/categories.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/geoserverdomain.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/geoserverworkspace.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/ogclayer.json
python3 ../project/manage.py loaddata ../project/fixtures/opengeodata/webgisproject.json

echo "End process"