#!/usr/bin/env python3

import cgi,cgitb
import secret
import requests
from http import cookies
from templates import secret_page


form = cgi.FieldStorage()

username= form.getvalue('username')
password= form.getvalue('password')

if username == secret.username and password == secret.password:
    C = cookies.SimpleCookie()
    C["Login"] = True
    C["Username"] = secret.username
    C["Password"] = secret.password
    print(C)
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("</head>")
    print("<body>")
    print("<p><b>Welcome,</b> %s <b>Pst! I know your password is</b> %s<p>" % (secret.username,secret.password))
    print("</body>")
    print("</html>")
    


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI program</title>")
print("</head>")
print("<body>")
print("<p><b>USername</b> %s <b>password</b> %s<p>" % (username,password))
print("</body>")
print("</html>")




