#!/bin/sh

# shellcheck disable=SC2164
cd /app

# wait for db
sleep 5

python manage.py migrate
python manage.py initadmin

python manage.py runserver 0.0.0.0:8000
