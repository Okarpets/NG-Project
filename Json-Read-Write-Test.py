import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from openpyxl import load_workbook 
from bs4 import BeautifulSoup
import json

#from jsonpath_ng import parse
# SHOW JSON DETAIL
#def json_detail(element_order):
#    with open("scenario.json", "r") as file:
#        result = [m.value for m in parse('$..{}'.format(element_order)).find(json.loads(file.read()))]
        #Parising user order and find it on that json file
#        for element_order in (result):
#            print(result)

#json_detail(element_order)




file = open("test.json", "r")
file = json.load(file) 
for lines in file:
    id = lines['scen']
    url = lines['url']
    code_get = lines['get']
    if code_get == "1":
        site = requests.get(url)
        code_get = site.status_code
    else:
        code_get = "The operation was not requested"
    code_post = lines['post']
    if code_post == "1":
        site = requests.post(url)
        code_post = site.status_code
    else:
        code_post = "The operation was not requested"
    u_id = lines['htmlid']
    if u_id != "0":
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        u_id = soup.find_all(id='{0}'.format(u_id))
        html = site.text # GET HTML OF THE SITE
        u_id = "id=\"{}\"".format(u_id) # ID SEARCH
        if u_id in html:
            u_id = "The element IS on the page"
        else:
            u_id = "The element ISN'T on the page"
    else:
        u_id = "The operation was not requested"
    u_tag = lines['htmltag']
    if u_tag != "0":
        site = requests.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        u_tag = soup.find_all('{0}'.format(u_tag))
        if u_tag == []:
            u_tag = "Tag ISN'T HERE"
        if u_tag != []:
            u_tag = "Tag IS here"
    else:
        u_tag = "The operation was not requested"
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['ScenarioResults'] #List in 'TestResult.xlsx'
    xlsx.append([id,url,code_get,code_post,u_id,u_tag]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()