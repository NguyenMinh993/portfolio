# +++++++++++ DJANGO +++++++++++
# This file is required for Django projects.
# It's been set up for you automatically.
# You can find more information in the Django docs:
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/

import os
import sys

# Add your project's directory to the Python path.
# This is the directory that contains your 'manage.py' file.
# Make sure the path is correct for your username and project folder name.
path = '/home/NguyenMinh993/djangoportfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the DJANGO_SETTINGS_MODULE environment variable.
# This tells Django where to find your settings.py file.
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoProject.settings'

# Import the Django WSGI application.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()