release: python manage.py migrate
web: gunicorn --pythonpath="$PWD/xpay" wsgi:application
worker: python manage.py rqworker high default low