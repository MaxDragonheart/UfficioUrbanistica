![GitHub](https://img.shields.io/github/license/MaxDragonheart/UfficioUrbanistica?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/MaxDragonheart/UfficioUrbanistica?style=for-the-badge)
![GitHub milestones](https://img.shields.io/github/milestones/open/MaxDragonheart/UfficioUrbanistica?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/MaxDragonheart/UfficioUrbanistica?style=for-the-badge)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/MaxDragonheart/UfficioUrbanistica?label=Release%20Date&style=for-the-badge)

# Ufficio Urbanistica

### Geo-CMS per la condivisione di notizie da parte degli uffici tecnici della PA

*Ufficio Urbanistica* usa *[Bootstrap Italia template for Django](https://github.com/UniversitaDellaCalabria/design-django-theme)* per rispettare le nuove linee guida di design per i servizi web della PA.
Integra e sostituisce [OpenGeoData](https://github.com/MaxDragonheart/OpenGeoData).

## Project startup

### 1 - Build and start the containers
If Apache2 is up, it's necessary to put it down.

Check Apache2 status: `sudo systemctl status apache2`

Stop Apache2: `sudo systemctl stop apache2`

`docker compose -f COMPOSE.YML up -d --build`

### 2 - Make DB table and collact statics
`docker exec -it WEBSITE-CONTAINER-NAME bash`
`./start_project-production.sh`

NB: to login into project website you must use the default user `ufficio` with the default password `urbanistica`. Remember to create a new super user after the first access to the administration site.

### 3 - Get geosources from Geoserver's container
To login for the first time into Geoserver you must use as user `admin` and as password `geoserver`. Remember to change it after the first logging in.
Create a `Workspace`, so add a `Store` using some geodata. Login into website and add the Geoserver's domain. That domain is
the url of Geoserver's container. That url starts with `container_name` there is into `docker-compose`.

E.g: `container_name: geoserver-staging`, `WORKSPACE: test`
The url is: `http://geoserver-staging:8080`. The domain url is: `http://geoserver-staging:8080/geoserver/test/wms`