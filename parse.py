#!/usr/bin/python3.4
import re
from bs4 import BeautifulSoup

UrlPrefix = "https://www.google.com"

soup = BeautifulSoup(open("index.html"),"lxml")
result = soup.find_all(title=True,href=re.compile("^/video"))

# Extract `href` part from `result` list   
UrlPart = [tag['href'] for tag in result]

# Construct completed url
CompleteUrl = [UrlPrefix+url for url in UrlPart]

for elem in CompleteUrl:
	print(elem)
print(len(CompleteUrl))
