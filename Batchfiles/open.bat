@ECHO OFF
start cmd.exe /C "cd nasuh\env\ && .\Scripts\activate && cd .\src && python manage.py runserver "
start "C:\Program Files\Google\Chrome\Application\chrome.exe" "http://127.0.0.1:8000/"