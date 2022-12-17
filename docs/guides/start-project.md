# Project startup

## 1 - Build and start the containers
`docker compose -f COMPOSE.YML up -d --build`

## 2 - Make DB table and collact statics
`docker exec -it WEBSITE-CONTAINER-NAME bash`
`./start_project-production.sh`

## 3 - Get geosources from Geoserver's container

Create a `Workspace`, so add a `Store` using some geodata. Login into website and add the Geoserver's domain. That domain is
the url of Geoserver's container. That url starts with `container_name` there is into `docker-compose`.

E.g: `container_name: geoserver-staging`, `WORKSPACE: test`
The url is: `http://geoserver-staging:8080`. The domain url is: `http://geoserver-staging:8080/geoserver/test/wms`
