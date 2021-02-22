Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c cd /d C:\kira_takip\ & venv_kira\Scripts\activate.bat & cd /d C:\kira_takip\kod & python manage.py runserver 2626"
oShell.Run strArgs, 0, false