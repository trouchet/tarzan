"""
This module configures the Celery worker for background task 
processing in a Django project.

It sets up the necessary environment and configurations for Celery to 
work with Django.This module should be imported and executed when starting 
the Celery worker.

The following functions and settings are defined in this module:
- `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')`: 
    Sets the default Django settings module for the 'celery' program.

- `app = Celery('src')`: 
    Creates a Celery instance named 'src' for managing tasks.

- `app.config_from_object('django.conf:settings', namespace='CELERY')`:  Loads configuration 
    settings from the Django settings module for Celery, using the 'CELERY' namespace.

- `app.autodiscover_tasks()`: Discovers and auto-imports task modules from 
    all installed Django apps.

Make sure to import and execute this module to configure Celery for your Django project.
"""

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

app = Celery('src')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover and auto-import tasks from all installed apps
app.autodiscover_tasks()
