import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from openpyxl import load_workbook 
from bs4 import BeautifulSoup
import json

def read(p_name):
    file = open("{0}.json".format(p_name), "r")
    file = json.load(file) 
    for lines in file:

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


        if code_get == "1":
            site = requests.post(url)
            post_order = site.status_code
        if code_get == "2":
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
            if u_id != []:
                u_id = "The element IS on the page"
            else:
                u_id = "The element ISN'T on the page"
        else:
            u_id = "The operation was not requested"
        
        
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
        xlsx.append([url,code_get,code_post,u_id,u_tag]) #Adding that data in xlsx file
        lst.save(file) #REMEMBER THE WRITING RULES
        lst.close()
    print("\n\t\tAll the scenario was processed\n")



read("testy")


#match order: # Getting the operation from the request
 #           case "1":
#
 #               par_order = str(input("\tDo you want to add params? (Y/ )\n"))
  #              if par_order == 'Y' or par_order == 'y':
   #                 file_name = str(input("\tEnter name of the json-file with params\n"))
    #                file = open("{}.json".format(file_name), "r")
                  #  u_data = json.load(file)
                 #   site = requests.get(url, params=json.dumps(u_data))
                #    get = site.status_code
               # else:
              #      site = requests.get(url)
             #       get = site.status_code

            #case "2":
                                
          #      par_order = str(input("\tDo you want to add data? (Y/ )\n"))
          #      if par_order == 'Y' or par_order == 'y':
           #         file_name = str(input("\tEnter name of the json-file with data\n"))
           #         file = open("{}.json".format(file_name), "r")
           #         u_data = json.load(file)
           #         site = requests.post(url, data=json.dumps(u_data))
           #         post = site.status_code
           #     else:
           #         site = requests.post(url)
           #         post = site.status_code
