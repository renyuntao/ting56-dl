#!/usr/bin/python3.4
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

UrlPrefix = "http://www.ting56.com"

html = urlopen("http://www.ting56.com/mp3/4704.html")
soup = BeautifulSoup(html, "lxml")
result = soup.find_all(title=True,href=re.compile("^/video"), limit=1)

# Extract `href` part from `result` list   
UrlPart = [tag['href'] for tag in result]

# Construct completed url
CompleteUrl = [UrlPrefix+url for url in UrlPart]

# Use PhantomJs browser to get content that generate by Javascript
driver = webdriver.PhantomJS(executable_path="/mnt/73G/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")

for url in CompleteUrl:
	# Scrap Web page that URL is `url`
	driver.get(url)

	# Get content of Web page that URL is `url`
	pageSource = driver.page_source

	# Use `BeautifulSoup` to parse this content
	bsObj = BeautifulSoup(pageSource, "lxml")

	# Get tag that name is `source`
	tag = bsObj.find("source")

	# Get the attribute `src` of tag `source`
	print(tag['src'])

driver.close()
