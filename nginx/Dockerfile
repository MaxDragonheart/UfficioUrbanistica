# syntax=docker/dockerfile:1

# Official Ubuntu Image as Layer
FROM ubuntu:22.04 as os
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive
# Update&Upgrade Ubuntu
RUN apt update && apt upgrade -y

FROM os as nginx
RUN apt install nginx -y \
    && apt-get install software-properties-common -y

FROM nginx as certbot
RUN apt install python3-certbot-nginx -y
COPY files/default.conf /etc/nginx/conf.d

EXPOSE 80/tcp
EXPOSE 443/tcp

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]