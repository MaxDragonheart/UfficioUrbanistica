#!/usr/bin/env bash

## Prepare log files and start outputting logs to stdout
echo "Make log files"
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log

echo "Move to project directory"
cd project

echo "Project in progress.."
poetry run gunicorn project.wsgi:application \
    --name project \
    --bind 0.0.0.0:"${PROJECT_PORT}" \
    --workers 3 \
    --log-level=debug \
    --error-logfile=../logs/gunicorn.log \
    --access-logfile=../logs/gunicorn-access.log \
"$@"