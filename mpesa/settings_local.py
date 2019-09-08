# Please copy this as a settings_local.py on the same directory and ensure to not add to version control, i.e. git ignore this file. Adjust the variables to meet your own settings
#To automate Local and Production server settings
import socket
import os


# Paths for project root, package root and base directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

if socket.gethostname() == 'josemachava':
    ALLOWED_HOSTS = ['*']


    #DATABASES = {
    #    'default': {
     #       'ENGINE': 'django.db.backends.sqlite3',
    #        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      #  }
   # }

    DATABASES = {
       'default': {
          'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'marketv3',
            'USER': 'josemachava',
           'PASSWORD': '849394995',
           'HOST':  'localhost',
           'PORT':  '5432',

        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'mpesa', 'static'),
    )


Has_Local_Settings = True
DEBUG = True