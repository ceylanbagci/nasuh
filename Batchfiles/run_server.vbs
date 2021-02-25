Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c cd /d D:\nasuh\ & env\Scripts\activate.bat & cd /d D:\nasuh\ & python manage.py runserver"
oShell.Run strArgs, 0, false