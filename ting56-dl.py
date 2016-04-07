#!/usr/bin/python3.4
import re
import datetime
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.request import URLError
from bs4 import BeautifulSoup
from selenium import webdriver

UrlPrefix = "http://www.ting56.com"

html = ''

try:
	html = urlopen("http://www.ting56.com/mp3/4704.html")
except URLError:
	print('URLError: Name or service not known, network may not accessible.')
	exit(1)

soup = BeautifulSoup(html, "lxml")
result = soup.find_all(title=True,href=re.compile("^/video"), limit=2)

# Extract `href` part from `result` list   
UrlPart = [tag['href'] for tag in result]

# Construct completed url
CompleteUrl = [UrlPrefix+url for url in UrlPart]

# Set browser's position
BrowserPosition = "/mnt/73G/phantomjs-2.1.1-linux-x86_64/bin/phantomjs"

# Use PhantomJs browser to get content that generate by Javascript
driver = webdriver.PhantomJS(executable_path=BrowserPosition)

fout = open('url.txt', 'w')

for url in CompleteUrl:
	print('url:',url)

	# Scrap Web page that URL is `url`
	driver.get(url)

	# Get content of Web page that URL is `url`
	pageSource = driver.page_source

	# Use `BeautifulSoup` to parse this content
	bsObj = BeautifulSoup(pageSource, "lxml")

	# Get tag that name is `source`
	tag = bsObj.find("source")

	# Write the attribute `tag` of tag `source`(i.e. url) to file `url.txt`
	fout.write(tag['src']+'\n')

	# Print information
	print('Get one...')

# Close file `url.txt`
fout.close()
# Closes the current window
driver.close()

#####################################################################
# Download the audio file from the URL that saved in file `url.txt` # 

# Read url from `url.txt`
fin = open('url.txt')
urls = fin.readlines()
fin.close

seq = 1

# Error information saved in file `error.log`
fout = open('error.log', 'a')

# Download file
for url in urls:
	url = url.rstrip('\n')

	try:
		urlretrieve(url, 'Downloads/file{0}'.format(seq))
	except URLError:
		fout.write(str(datetime.datetime.now()) + '   URLError: Name or service not known.   file{0} not download.\n'.format(seq))

	seq += 1

fout.close()
