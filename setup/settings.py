"""
Django settings for project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from re import findall
from pathlib import Path
from decouple import config
from drf_yasg.openapi import Info, Contact, License

import configparser

# Determine the path to the pyproject.toml file one folder above the current location
current_dir = os.path.dirname(__file__)
relative_py_tol_path = os.path.join(current_dir, '..', 'pyproject.toml')
pyproject_path = os.path.abspath(relative_py_tol_path)

# Create a configparser instance and read the pyproject.toml file
pyproject_config = configparser.ConfigParser()
pyproject_config.read(pyproject_path)

# Access values from the pyproject.toml file
project_name = pyproject_config['tool.poetry']['name']
project_version = pyproject_config['tool.poetry']['version']
project_description = pyproject_config['tool.poetry']['description']
project_authors = pyproject_config['tool.poetry']['authors']
project_license = pyproject_config['tool.poetry']['license']

# Extract authors' names and email addresses using regular expressions
author_pattern = r'(.*?) <(.*?)>'
author_matches = findall(author_pattern, project_authors)

# Create a list of dictionaries with author names and emails
author_info = [
    {'name': name.strip(), 'email': email.strip()} for name, email in author_matches
]

# Replace with the desired redirect URL
LOGIN_URL = '/api/profile/'

# Use the database model user for authentication
AUTH_USER_MODEL = 'auth.user'

# Use the database for session storage (recommended for production)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Use the default session serializer (JSON serializer is common)
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Set the session cookie name (optional but recommended for security)
SESSION_COOKIE_NAME = 'my_session_cookie'

# Set session timeout (in seconds)
SESSION_COOKIE_AGE = 3600  # 1 hour, adjust as needed

# Set whether the session cookie is secure (HTTPS only, recommended for
# production)
SESSION_COOKIE_SECURE = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'src',
    'rest_framework',
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

#
# NOTE: Replace with your API's terms of service URL
first_author = author_info[0]

api_info = Info(
    title=project_name,
    default_version=project_version,
    description=project_description,
    terms_of_service='',
    contact=Contact(name=first_author['name'], email=first_author['email']),
    license=License(name=project_license),
    authors=author_info,
)


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'},
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'DEFAULT_INFO': api_info,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_SETUP_DICT = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('POSTGRES_DB'),
    'USER': config('POSTGRES_USER'),
    'PASSWORD': config('POSTGRES_PASSWORD'),
    'HOST': config('POSTGRES_HOST'),
    'PORT': config('POSTGRES_PORT'),
}

DATABASES = {
    'default': DB_SETUP_DICT,
    'test': DB_SETUP_DICT,
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'EXCEPTION_HANDLER': 'setup.exceptions.custom_exception_handler',
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # new

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default logging
# https://docs.djangoproject.com/en/4.2/ref/logging/

LOGGING = {
    'version': 1,  # the dictConfig format version
    'disable_existing_loggers': False,  # retain the default loggers
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'general.log',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['file'],
        },
    },
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
}
