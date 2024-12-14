#!/bin/sh


# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
echo "Starting server..."
exec "$@"
