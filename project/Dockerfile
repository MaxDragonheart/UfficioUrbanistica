# syntax=docker/dockerfile:1
ARG PROJECT_NAME=UfficioUrbanistica_test
ARG DEBUG=1
ARG ALLOWED_HOSTS=*
ARG SECRET_KEY=test_secret_key
ARG DB_ENGINE=django.contrib.gis.db.backends.postgis
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
RUN apt-get install python3.8-venv

# GIS-OS as Layer
FROM gis-os as project-dependencies
# Set work directory
WORKDIR /app/web
# Environment variables
#ARG PROJECT_NAME=UfficioUrbanistica_test
ENV ENV_NAME=${PROJECT_NAME} \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    # https://python-poetry.org/docs#ci-recommendations
    POETRY_VERSION=1.2.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache
# Install Poetry
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}
# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
# Copy project requirements
COPY ./pyproject.toml ./pyproject.toml
# Project initialization
RUN poetry install --only main --no-root --no-ansi

# Project Dependencies as Layer
FROM project-dependencies as project
ENV SECRET_KEY=${SECRET_KEY} \
    DEBUG=${DEBUG} \
    ALLOWED_HOSTS=${ALLOWED_HOSTS} \
    PROJECT_PORT=${PROJECT_PORT} \
    DB_ENGINE=${DB_ENGINE} \
    DB_NAME=${DB_NAME} \
    DB_USER=${DB_USER} \
    DB_PASSWORD=${DB_PASSWORD} \
    DB_PORT=${DB_PORT} \
    DB_HOST=${DB_HOST}

# Create project directories
RUN mkdir -p project static-folder media-folder
COPY project project
COPY media-folder/demo_data media-folder/demo_data
RUN rm -rf project/fixtures
COPY scripts/migrate-collectstic.sh ./migrate-collectstic.sh
#COPY scripts/backup-fixtures.sh ./backup-fixtures.sh
COPY scripts/restore-fixtures.sh ./restore-fixtures.sh
COPY scripts/make-fixtures-folders.sh ./make_fixtures-folders.sh
COPY scripts/start_project-production.sh ./start_project-production.sh
RUN chmod +x **.sh

# Project as Layer
FROM project as gunicorn-setting-up
# Install Gunicorn
RUN poetry add gunicorn
# Create directory for logging files
RUN mkdir logs
# Copy adn active entrypoint
COPY scripts/entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]