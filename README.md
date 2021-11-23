# django_property
simple property database with django and postgres

python3 -m venv .env     # optional

source .env/bin/activate # optional

pip install -r requirements.txt

./manage.py migrate --run-syncdb

./manage.py runserver
