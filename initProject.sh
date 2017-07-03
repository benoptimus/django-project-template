pip install -r requirement.txt
python manage.py migrate --run-syncdb
python manage.py createsuperuser
