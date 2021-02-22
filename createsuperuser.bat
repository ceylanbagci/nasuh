@echo off
cmd /k "python -m venv env & env\Scripts\activate.bat & python manage.py createsuperuser & admin & admin@admin.com & 1234 & 1234 & y"