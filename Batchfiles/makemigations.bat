@ECHO OFF
cd nasuh
env\Scripts\activate
python manage.py migrate
python manage.py makemigrations


