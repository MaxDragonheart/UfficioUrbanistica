# Docker & Compose

## Build
Build: `docker build -t LAYER-NAME .`

Build with args: `docker build --build-arg ARG1=VALUE1 --build-arg ARG2=VALUE2 -t LAYER-NAME .`

## Run
Run and access to container: `docker run -it LAYER-NAME` 

Run and access to container using `.env`: `docker run --env-file /home/max/DEV/UfficioUrbanistica/.env -it LAYER-NAME` 

## Start
Start container: `docker container run -it -d --name CONTAINER-NAME -p 8081:8080 LAYER-NAME`

## Utility
List of active container: `docker ps`

List of images: `docker images`

Purge images and volumes: `docker system prune -a --volumes`

Reset containers: `docker compose -f COMPOSE.YML down -v`
