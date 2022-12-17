# Project Environment

The project use `.env` with the key below:
```markdown
# Generic Project Stuffs
PROJECT_NAME=test_project_env_docker
PROJECT_PORT=8301

# Django
DEBUG=False
ALLOWED_HOSTS="*"
CSRF_TRUSTED_ORIGINS=['http://domin.io', 'https://domin.io']
SECRET_KEY=build-your-secret-key

# DB Connection Parameters
DB_NAME=ufficiourbanistica
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=1983

# Geoserver Parameters
GS_VERSION=2.20.4
GS_DEMO_DATA=True
GS_HTTP_PORT=8302
GS_INITIAL_MEMORY=1G
GS_MAXIMUM_MEMORY=4G
TOMCAT_MAJOR=9
TOMCAT_MINOR=0
```
To generate secret key you can use [Djecrety](https://djecrety.ir/)