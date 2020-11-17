release: python manage.py migrate
web: gunicorn xpay.wsgi --timeout 15 --keep-alive 5 --log-level debug