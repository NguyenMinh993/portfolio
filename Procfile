web: python manage.py migrate && gunicorn --bind 0.0.0.0:$PORT --workers 3 DjangoProject.wsgi:application
release: python manage.py collectstatic --noinput