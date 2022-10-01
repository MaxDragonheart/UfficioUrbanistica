#!/usr/bin/env bash

## Prepare log files and start outputting logs to stdout
echo "Make log files"
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log

echo "Move to project directory"
cd personal_website

echo "Project in progress.."
exec gunicorn personal_website.wsgi:application \
    --name personal_website \
    --bind 0.0.0.0:"${PROJECT_PORT}" \
    --workers 3 \
    --log-level=debug \
    --error-logfile=../logs/gunicorn.log \
    --access-logfile=../logs/gunicorn-access.log \
"$@"