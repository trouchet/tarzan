#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 <port>"
    exit 1
}

# Check if the port argument is provided
if [ $# -ne 1 ]; then
    usage
fi

port="$1"

# Apply migrations
poetry run python manage.py migrate

# Creation of cache table
poetry run python manage.py createcachetable

# Collect static files
poetry run python manage.py collectstatic --noinput

# Start the Django development server
exec poetry run python manage.py runserver 0.0.0.0:"$port"
