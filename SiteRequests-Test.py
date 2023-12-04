import requests
from bs4 import BeautifulSoup

url = "http://google.com"
headers = {'Accept-Encoding': 'identity'}
site = requests.get(url)
html = site.text # GET HTML OF THE SITE
code = site.status_code # CODE OF GET REQUEST
search = BeautifulSoup(html, 'html.parser')
tag = search.find_all('') # TAG SEARCH
u_id = search.find(id='gbv') # ID SEARCH

#TEST-SUITE
print(code) #PASSED
print(html) #PASSED
print(u_id) #PASSED



