#!/usr/bin/python3.4
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

UrlPrefix = "https://www.ting56.com"

html = urlopen("http://www.ting56.com/mp3/4704.html")
soup = BeautifulSoup(html, "lxml")
result = soup.find_all(title=True,href=re.compile("^/video"), limit=2)

# Extract `href` part from `result` list   
UrlPart = [tag['href'] for tag in result]

# Construct completed url
CompleteUrl = [UrlPrefix+url for url in UrlPart]

for elem in CompleteUrl:
	print(elem)
print(len(CompleteUrl))
