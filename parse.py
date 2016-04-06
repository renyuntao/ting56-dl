#!/usr/bin/python3.4
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://www.ting56.com/video/4704-0-0.html"
driver = webdriver.PhantomJS(executable_path="/mnt/73G/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
print(url)
driver.get(url)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource, "lxml")
tag = bsObj.find("source")
print(tag['src'])
