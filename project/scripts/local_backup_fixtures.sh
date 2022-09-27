#!/usr/bin/env bash
# Useful only in development on local machine.
echo "Start backup"
echo "NOTE: use only in staging!!"

# Usermanager
echo "- make fixtures for Usermanager"
poetry run python3 ../project/manage.py dumpdata usermanager.userprofile --indent 2 > ../project/fixtures/usermanager/userprofile.json

# Standard Apps
echo "- make fixtures for Django's standard apps"
poetry run python3 ../project/manage.py dumpdata sites --indent 2 > ../project/fixtures/sites.json
poetry run python3 ../project/manage.py dumpdata flatpages --indent 2 > ../project/fixtures/flatpages.json

# Core
echo "- make fixtures for Core"
poetry run python3 ../project/manage.py dumpdata core.sitecustomization --indent 2 > ../project/fixtures/core/sitecustomization.json

# Link
echo "- make fixtures for Link"
poetry run python3 ../project/manage.py dumpdata link.link --indent 2 > ../project/fixtures/link/link.json

# Media
echo "- make fixtures for Media"
poetry run python3 ../project/manage.py dumpdata media.fileupload --indent 2 > ../project/fixtures/media/fileupload.json

# Sections
echo "- make fixtures for Sections"
poetry run python3 ../project/manage.py dumpdata sections.section --indent 2 > ../project/fixtures/sections/section.json
poetry run python3 ../project/manage.py dumpdata sections.sectionpost --indent 2 > ../project/fixtures/sections/sectionpost.json

# Open GeoData
echo "- make fixtures for Open GeoData"
poetry run python3 ../project/manage.py dumpdata opengeodata.categories --indent 2 > ../project/fixtures/opengeodata/categories.json
poetry run python3 ../project/manage.py dumpdata opengeodata.geoserverdomain --indent 2 > ../project/fixtures/opengeodata/geoserverdomain.json
poetry run python3 ../project/manage.py dumpdata opengeodata.geoserverworkspace --indent 2 > ../project/fixtures/opengeodata/geoserverworkspace.json
poetry run python3 ../project/manage.py dumpdata opengeodata.ogclayer --indent 2 > ../project/fixtures/opengeodata/ogclayer.json
poetry run python3 ../project/manage.py dumpdata opengeodata.webgisproject --indent 2 > ../project/fixtures/opengeodata/webgisproject.json

echo "End process"