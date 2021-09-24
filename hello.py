#!/usr/bin/env python3
import os,json
from http import cookies
import requests
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")

print(os.environ)
json_object = json.dumps(dict(os.environ),indent = 4)
print(json_object)

query = dict(os.environ)
print("<p>QUERY_STRING =",query["QUERY_STRING"],"</p>")

print("<p>Browser =",query["HTTP_USER_AGENT"],"</p>")

#print("<p>Browser =",query["HTTP_USER_AGENT"],"</p>")
#r = requests.get('http://localhost:8080')
#print(r.cookies['Username'])

