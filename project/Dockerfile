# syntax=docker/dockerfile:1
ARG PROJECT_NAME=UfficioUrbanistica_test
ARG DEBUG=1
ARG ALLOWED_HOSTS='*'
ARG SECRET_KEY=test_secret_key
ARG DB_NAME=test_db_docker
ARG DB_USER=postgres
ARG DB_PASSWORD=30092022
ARG DB_PORT=5432
ARG DB_HOST=localhost
ARG PROJECT_PORT=8301
ARG ALLOWED_HOSTS=${ALLOWED_HOSTS}
ARG PROJECT_PORT=${PROJECT_PORT}

# Ubuntu Lib GIS Image as Layer
FROM maxdragonheart/ulgis:latest as gis-os
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive
# Update&Upgrade Ubuntu
RUN apt update && apt upgrade -y

# GIS-OS as Layer
FROM gis-os as project-dependencies
# Set work directory
WORKDIR /app/web
# Environment variables
ENV ENV_NAME=${PROJECT_NAME} \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry is already installed in ULGIS
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
# Copy project requirements
COPY ./pyproject.toml ./pyproject.toml
# Project initialization
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --only main --no-root

# Project Dependencies as Layer
FROM project-dependencies as gunicorn
# Install Gunicorn
RUN poetry add gunicorn
# Create directory for logging files
RUN mkdir logs
# Copy adn active entrypoint
COPY scripts/entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

# Gunicorn as Layer
FROM gunicorn as build-project
ENV SECRET_KEY=${SECRET_KEY} \
    DEBUG=${DEBUG} \
    ALLOWED_HOSTS=${ALLOWED_HOSTS} \
    PROJECT_PORT=${PROJECT_PORT} \
    DB_NAME=${DB_NAME} \
    DB_USER=${DB_USER} \
    DB_PASSWORD=${DB_PASSWORD} \
    DB_PORT=${DB_PORT} \
    DB_HOST=${DB_HOST}

# Create project directories
RUN mkdir -p project static-folder media-folder
COPY project project
RUN rm -rf project/project/.env
COPY media-folder/demo_data media-folder/demo_data
RUN rm -rf project/fixtures

COPY scripts/production/backup_restore/backup-fixtures.sh ./backup_restore/backup-fixtures.sh
COPY scripts/production/backup_restore/restore-fixtures.sh ./backup_restore/restore-fixtures.sh

COPY scripts/production/migrate-collectstic.sh ./migrate-collectstic.sh
COPY scripts/production/start_project-production.sh ./start_project-production.sh

RUN chmod +x **.sh

