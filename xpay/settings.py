"""
Django settings for xpay project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import django_heroku
import dj_database_url
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm+mde9c7#1#b^=kdk$@r7qqy7qh(6*=u&t3##+z7zxeb-rva@$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'mpesa',
    'account',
    'payment',
    'uria',
    'xpay',
    'send',
    'wordpress',
    'dashboard',
    'crispy_forms',
    'graphene_django',
    "django_rq",


]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
GRAPHENE = {
    'SCHEMA': 'xpay.schema.schema'
}





RQ_QUEUES = {

    'with-sentinel': {
        'SENTINELS': [('localhost', 26736), ('localhost', 26737)],
        'MASTER_NAME': 'redismaster',
        'DB': 0,
        'PASSWORD': 'secret',
        'SOCKET_TIMEOUT': None,
        'CONNECTION_KWARGS': {
            'socket_connect_timeout': 0.3
        },
    },
    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'), # If you're on Heroku
        'DEFAULT_TIMEOUT': 500,
    },

}




EMAIL_HOST = 'mail.kutiva.co.mz'
EMAIL_PORT = 26
EMAIL_HOST_USER = 'noreply@kutiva.co.mz'
EMAIL_HOST_PASSWORD = '849394995Jose'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@kutiva.co.mz'

AUTH_USER_MODEL = 'account.User'
LOGIN_URL='signin'
LOGOUT_REDIRECT_URL = 'index'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#Authentication backends
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
ROOT_URLCONF = 'xpay.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['xpay/templates'],
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

WSGI_APPLICATION = 'xpay.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
try:
    from .settings_local import *
except ImportError:

    ALLOWED_HOSTS = ["*"]


    #ADMINS = [('Arnaldo Govene', 'arnaldo.govene@outlook.com'), ('Guidione  Machava', 'geral.market.co.mz@gmail.com'),
     #('Jose Machava',  'josesmachava@gmail.com'), ]

    # Parse database configuration from $DATABASE_URL
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
    # Enable Persistent Connections



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Maputo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'xpay', 'static'),
)

django_heroku.settings(locals())
