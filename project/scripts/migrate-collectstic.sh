#!/usr/bin/env bash
echo "- Start DB and collect static files"

echo "1. Build DB tables"
poetry run python3 project/manage.py migrate

echo "2. Collect static files"
poetry run python3 project/manage.py collectstatic --noinput