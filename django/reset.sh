rm db.sqlite3
rm -rf woot/registry/migrations
python manage.py makemigrations registry
python manage.py migrate