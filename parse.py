#!/usr/bin/python3.4
from urllib.request import urlopen

url = "http://www.ting56.com/video/4704-0-57.html"

html = urlopen(url)
content = html.read().decode('cp936')
print(content)
