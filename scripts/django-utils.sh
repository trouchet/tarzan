#!/bin/bash

# Apply migrations
poetry run python manage.py migrate

# Collect static files
poetry run python manage.py collectstatic --noinput

# Start the Django development server
exec poetry run python manage.py runserver 0.0.0.0:8000
