#!/usr/bin/env bash
echo "Create STAGING DB..."

read -p 'DB name: ' DB_NAME

if [[ "$DB_NAME" == "postgres" ]]; then
  echo "You mustn't create postgres!"

else

sudo su postgres <<EOF
  psql -c "CREATE DATABASE $DB_NAME;"
  psql -c "CREATE EXTENSION postgis;"
  echo "Database '$DB_NAME' created."
  psql -c "\l"  # List all DBs
EOF

fi