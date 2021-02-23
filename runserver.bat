@echo off
<<<<<<< HEAD
cmd /k "cd /d D:\nasuh\ & env\Scripts\activate"
SET PROPER_GTK_FOLDER=C:\Program Files\GTK3-Runtime Win64\bin
SET PATH=%PROPER_GTK_FOLDER%;%PATH%
cmd /k "python manage.py runserver"
pause
=======
cmd /k "cd /d C:\kira_takip\ & venv_kira\Scripts\activate.bat & cd /d    C:\kira_takip\kod & python manage.py runserver"
>>>>>>> 9363170324822e3bf0ab76f1f61e4280ef9ae98b
