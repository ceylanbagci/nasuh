@echo off
cmd /k "cd /d D:\nasuh\ & env\Scripts\activate"
SET PROPER_GTK_FOLDER=C:\Program Files\GTK3-Runtime Win64\bin
SET PATH=%PROPER_GTK_FOLDER%;%PATH%
cmd /k "python manage.py runserver"
pause
