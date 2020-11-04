# Please copy this as a settings_local.py on the same directory and ensure to not add to version control, i.e. git ignore this file. Adjust the variables to meet your own settings
#To automate Local and Production server settings
import socket
import  os


if socket.gethostname() == 'josemachava':	#ensure your local machine hostname is used
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join('db.sqlite3'),
        }
    }
DEBUG_PROPAGATE_EXCEPTIONS = False
WHITENOISE_AUTOREFRESH = True