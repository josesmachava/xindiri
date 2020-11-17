release: python manage.py migrate
web: gunicorn --pythonpath="$PWD/xpay" config.wsgi:application
worker: python xpay/manage.py rqworker high default low