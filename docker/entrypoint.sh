#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput
# Run server
# python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 -t 2400 zaki.wsgi --log-level debug
