#!/bin/sh

# shellcheck disable=SC2164
cd /app

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
