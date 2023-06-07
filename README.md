py -3 -m venv .venv

python manage.py createsuperuser

python manage.py migrate
python manage.py makemigrations

django-admin startproject league
django-admin startapp league_api

python manage.py runserver