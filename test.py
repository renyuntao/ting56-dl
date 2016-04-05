#!/usr/bin/python3.4
from urllib.request import urlopen

html = urlopen("http://www.ting56.com/mp3/4704.html")
content = html.read().decode('cp936')
print(content)
