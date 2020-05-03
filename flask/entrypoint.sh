#!/bin/sh

# Check for env.sh and execute if present
if [ -f /var/www/flask/env.sh ]; then
   . /var/www/flask/env.sh
fi

# TODO
# Remove later
#export POSTGRES_URL="postgres_db:5432"
#export POSTGRES_USER="admin"
#export POSTGRES_PW="password"
#export POSTGRES_DB="heavyweight"

# Serve flask application using uwsgi
uwsgi --ini /etc/uwsgi.ini --chdir /var/www/flask
