#!/bin/sh


# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate
python manage.py shell -c "exec(open('data/1_data_for_chart.py', encoding='utf-8').read())"
python manage.py shell -c "exec(open('data/2_data_for_all_courses.py', encoding='utf-8').read())"
python manage.py shell -c "exec(open('data/3_data_for_prereq_coreq.py', encoding='utf-8').read())"
python manage.py shell -c "exec(open('data/4_map_courses_data.py', encoding='utf-8').read())"
# Start the Django development server
echo "Starting server..."
exec "$@"
