rm -r catalogue/migrations
mkdir catalogue/migrations
touch catalogue/migrations/__init__.py
python manage.py flush
