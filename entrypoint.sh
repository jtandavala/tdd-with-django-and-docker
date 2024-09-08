#!/bin/sh

if [ "$ENVIRONMENT" = "production" ]; then
    echo "Running in production mode"
    exec poetry run gunicorn -c gunicorn.conf.py
elif [ "$ENVIRONMENT" = "development" ]; then
    echo "Running in development mode"
    poetry install --no-root
    exec poetry run python manage.py runserver 0.0.0.0:8000
else
    echo "ENVIRONMENT variable is not set"
fi