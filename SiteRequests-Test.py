import requests
from bs4 import BeautifulSoup

url = "http://google.com"
headers = {'Accept-Encoding': 'identity'}
site = requests.get(url)
html = site.text # GET HTML OF THE SITE
search = BeautifulSoup(html, 'html.parser')
do = 'content'
u_id = search.find_all(id=do) # ID SEARCH

#TEST-SUITE
print(u_id) #PASSED



