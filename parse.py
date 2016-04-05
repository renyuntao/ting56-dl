#!/usr/bin/python3.4
import re
from bs4 import BeautifulSoup

UrlPrefix = "https://www.google.com"

soup = BeautifulSoup(open("index.html"),"lxml")
result = soup.find_all(title=True,href=re.compile("^/video"))

for elem in result:
	print(UrlPrefix + elem['href'])
print(len(result))
