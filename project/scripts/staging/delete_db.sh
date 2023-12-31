#!/usr/bin/env bash
echo "Delete STAGING DB..."

read -p 'DB name: ' DB_NAME

if [[ "$DB_NAME" == "postgres" ]]; then
  echo "You mustn't delete postgres!"

else

sudo su postgres <<EOF
  psql -c "DROP DATABASE $DB_NAME;"
  echo "Database '$DB_NAME' deleted."
  psql -c "\l"  # List all DBs
EOF
fi


