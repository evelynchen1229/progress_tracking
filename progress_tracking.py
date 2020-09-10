import mechanize
import cookiejar
#from cookiejar import FileCookieJar as fj
from http import cookiejar
from bs4 import BeautifulSoup
#from selenium import webdriver
import urllib
from urllib import request
import requests

import html5lib

br = mechanize.Browser()
cj = cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders=[('User-agent','Chrome')]

br.open('https://auth.freecodecamp.org/login?state=g6Fo2SA5NUMzcWxNbTh4aDlpeldOaHRwaDRsS2EwUjJZVDZrZaN0aWTZIDBsUWpnNU5vVlBCMkxUWDBBWmVWaExWTzRmZkRHalVzo2NpZNkgYVVEdjlqVnFUZnhCUkUxbDYwTkE1QWY3eVRDR0U0Y3k&client=aUDv9jVqTfxBRE1l60NA5Af7yTCGE4cy&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fapi.freecodecamp.org%2Fauth%2Fauth0%2Fcallback&scope=openid%20profile%20email')
#for f in br.forms():
#	print (f)
br.select_form(nr=0)

for control in br.form.controls:
	print(control)
email = br.form.find_control('email')
email.value = 'evelynchen1229@gmail.com'
print(email)
#submit_response = br.submit()

br.select_form(nr=1)
code = br.form.find_control('code')
code.value = '099506'
print(code)
#submit_response=br.submit()


br.open('https://www.freecodecamp.org/learn/?messages=success%5B0%5D%3DSuccess%2521%2520You%2520have%2520signed%2520in%2520to%2520your%2520account.%2520Happy%2520Coding%2521').read()


## webscraping to get a clean list/dataframe of main topic and related subtopics

## from Freecodecamp
#print ('import modules')
#import requests
#from bs4 import BeautifulSoup
#import urllib
#import urllib.request
#import re
#
url = r"""
https://www.freecodecamp.org/learn/?messages=success%5B0%5D%3DSuccess%2521%2520You%2520have%2520signed%2520in%2520to%2520your%2520account.%2520Happy%2520Coding%2521"""
#
response=requests.get(url)
print(response)
soup = BeautifulSoup(response.text,"html.parser")
print(soup)
#
table = soup.find('div',attrs = {'data-test-label':'learn-curriculum-map'})
#
print(table)
