#!/usr/bin/env bash
echo "Create STAGING .env ..."

read -p 'Insert secret key. To create it you can use https://djecrety.ir/: ' CREATE_KEY
read -p 'Insert DB_NAME: ' DB_NAME

MAIN_PATH="./../../project/project/"
FILENAME=".env"
FILE_PATH="$MAIN_PATH""$FILENAME"

touch $FILE_PATH

echo "SECRET_KEY='$CREATE_KEY'" >> $FILE_PATH
echo "DB_ENGINE=django.contrib.gis.db.backends.postgis" >> $FILE_PATH
echo "DEBUG=0" >> $FILE_PATH
echo "DB_NAME=$DB_NAME" >> $FILE_PATH
echo "DB_USER=postgres" >> $FILE_PATH
echo "DB_PASSWORD=1983" >> $FILE_PATH
echo "DB_HOST=localhost" >> $FILE_PATH
echo "DB_PORT=5432" >> $FILE_PATH

echo "File craeted in '$FILE_PATH'"