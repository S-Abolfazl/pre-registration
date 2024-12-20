FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "find . -path './*migrations/*' -not -name '__init__.py' -delete && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py shell -c 'exec(open(\"data/1_data_for_chart.py\", encoding=\"utf-8\").read())' && \
    python manage.py shell -c 'exec(open(\"data/2_data_for_all_courses.py\", encoding=\"utf-8\").read())' && \
    python manage.py shell -c 'exec(open(\"data/3_data_for_prereq_coreq.py\", encoding=\"utf-8\").read())' && \
    python manage.py shell -c 'exec(open(\"data/4_map_courses_data.py\", encoding=\"utf-8\").read())' && \
    python manage.py collectstatic --noinput && \
    python manage.py runserver 0.0.0.0:8000"]