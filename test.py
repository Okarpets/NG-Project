import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from openpyxl import load_workbook 
from bs4 import BeautifulSoup
import json


def handle(lines, p_name):
        scen_id = lines['id']
        url = lines['url']
        code_get = lines['get']
        get_params = lines['params']
        code_post = lines['post']
        post_data = lines['data']
        u_id = lines['htmlid']
        u_tag = lines['htmltag']

        if code_get == "1":
            site = requests.get(url)
            get_order = site.status_code
        if code_get == "2":
            try:
                file = open("{}.json".format(get_params), "r")
                u_data = json.load(file)
                site = requests.get(url, params=json.dumps(u_data))
                get_order = site.status_code
            except Exception:
                get_order = "Uncorrectly requests"
        else:
            get_order = "The operation was not requested"


        if code_post == "1":
            site = requests.post(url)
            post_order = site.status_code
        if code_post == "2":
            try:
                file = open("{}.json".format(post_data), "r")
                u_data = json.load(file)
                site = requests.post(url, data=json.dumps(u_data))
                post_order = site.status_code
            except Exception:
                post_order = "Uncorrectly requests"
        else:
            post_order = "The operation was not requested"
        

        if u_id != "0":
            site = requests.get(url)
            soup = BeautifulSoup(site.text, 'html.parser')
            u_id = soup.find_all(id='{0}'.format(u_id))
            if u_id == []:
                u_id = "The element ISN'T on the page"
            else:
                u_id = "The element IS on the page"
        else:
            u_id = "The operation was not requested"
        

        if u_tag != "0":
            print(u_tag)
            site = requests.get(url)
            soup = BeautifulSoup(site.text, 'html.parser')
            u_tag = soup.find_all('{0}'.format(u_tag))
            print(u_tag)
            if u_tag == []:
                u_tag = "Tag ISN'T HERE"
            else:
                u_tag = "Tag IS here"
        else:
            u_tag = "The operation was not requested"
        file = 'TestResults.xlsx' #Create or open file with that name
        lst = load_workbook(file) #It is depend on save and close command
        xlsx = lst['ScenarioResults'] #List in 'TestResult.xlsx'
        xlsx.append([scen_id,url,get_order,post_order,u_id,u_tag,p_name]) #Adding that data in xlsx file
        lst.save(file) #REMEMBER THE WRITING RULES
        lst.close()


def read(p_name, p_id):
    if p_id == "1":
        file = open("{0}.json".format(p_name), "r")
        file = json.load(file) 
        for lines in file:
            handle(lines, p_name)
        print("\n\t\tAll the scenario was processed\n")
    if p_id == "3":  
        with open("{0}.json".format(p_name), "r") as file:
            js_file = json.load(file)
            file.close()
            for elem in js_file:
                if str(elem['id']) == str(p_id):
                    handle(elem, p_name)


read("testy", "3")


