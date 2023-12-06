import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from openpyxl import load_workbook 
from bs4 import BeautifulSoup
import json
#THIS FILE WAS CREATED AS A COLLECTION OF TEAMS MODELS, 
#THEIR DESCRIPTIONS AND FURTHER DEVELOPMENT


#COMAND 0 - HELP
#THIS COMMAND WILL WRITE A MANUAL FOR USING THE PROGRAM
def help():
    print(
    "This program was created as a website tester, below you can see a list of existing commands:\n\n" +
    "\t-help -- Write a manual for using the program\n" +
    "\t-code_get <url> -- Returns the code from your get requests to the url\n" +
    "\t-code_post <url> -- Returns the code from your post requests to the url\n" +
    "\t-byid <url> <id> -- Returns the STATIC HTML element from your get requests to the url by id\n" +
    "\t-bytag <url> <tag> -- Returns the STATIC HTML element from your get requests to the url by tag\n" +
    "\t-create <file_name> -- Create scenario in document\n" +
    "\t-read <file_name> -- Read document with scenario\n"  
    )
    work()


#COMMAND 1 - CODE_GET
#RETURNS THE CODE FROM YOUR GET REQUESTS TO THE URL
def code_get(p_url):
    try:
        url = p_url
        try:
            site = requests.get(url)
        except Exception:
            print("\tInvalid values\n")
            work()
        code = site.status_code # CODE OF GET REQUEST
        print("\tReturned сode: " + str(code) + '\n')
    except ConnectionError: 
        print("\tConnection error\n")
    except Timeout:
        print("\tThe request timed out\n")

    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['CodeGetResults'] #List in 'TestResult.xlsx'
    xlsx.append([url,code]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()


#COMMAND 2 - CODE_POST
#RETURNS THE CODE FROM YOUR POST REQUESTS TO THE URL
def code_post(p_url):
    try:
        url = p_url
        try:
            site = requests.post(url)
        except Exception:
            print("\tInvalid values\n")
            work()
        code = site.status_code # CODE OF POST REQUEST
        print("\tReturned сode: " + str(code) + '\n')
    except ConnectionError: 
        print("\tConnection error\n")
    except Timeout:
        print("\tThe request timed out\n")

    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['CodePostResults'] #List in 'TestResult.xlsx'
    xlsx.append([url,code]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()


#COMMAND 3 - ELEMENT BY ID
#RETURNS THE HTML ELEMENT FROM YOUR GET REQUESTS TO THE URL BY ID
def byid(p_url, p_id):
    url = p_url
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    u_id = soup.find_all(id='{0}'.format(p_id))
    html = site.text # GET HTML OF THE SITE
    u_id = "id=\"{}\"".format(p_id) # ID SEARCH
    if u_id in html:
        reslt = "The element IS on the page"
    else:
        reslt = "The element ISN'T on the page"
    print('\t' + reslt + '\n')
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    #xlsx = lst['ElementById'] #List in 'TestResult.xlsx'
    #xlsx.append([p_id,url,reslt]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()


#COMAND 4 - FORMATS .XLSX DOCUMENT
#FORMATS THIS FILE BY ADDING THE NECESSARY SHEETS, DELETING UNNECESSARY ONES
def excel():
    file = 'TestResults.xlsx'
    lst = load_workbook(file) #It is depend on save and close command
    for sheet_name in lst.sheetnames:
        sheet = lst[(sheet_name)]
        lst.remove(sheet)
    lst.create_sheet('ScenarioResults')
    lst.create_sheet('CodeGetResults') # CREATE LISTS
    lst.create_sheet('CodePostResults')
    lst.create_sheet('ElementById')
    lst['CodeGetResults'].append(["Url","Returned Code"])
    lst['CodePostResults'].append(["Url","Returned Code"])
    lst['ElementById'].append(["Given Id","Url","Result"])
    lst['ScenarioResults'].append(["Scenario number","Url","Looked by id","Get requests","Post requests"])
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()

    
#COMMAND 5 - ELEMENT BY TAG
#RETURNS THE HTML ELEMENT FROM YOUR GET REQUESTS TO THE URL BY TAG
def bytag(p_url, p_tag):
    url = p_url
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    u_tag = soup.find_all('{0}'.format(p_tag))
    print(u_tag)
    print('\t' + str(u_tag) + '\n')
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    #xlsx = lst['ElementById'] #List in 'TestResult.xlsx'
    #xlsx.append([p_tag,url,reslt]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()


#CREATE SCENARIO MODEL (PROTOTYPE)
def create(p_name):
    file = open(f"{p_name}.json", 'w')
    file.write('[')
    command = "0"
    while True:
        id = str(input('\tEnter scenario id: '))
        url = str(input('\tEnter url: '))
        print(
            "\t\t\tNow pleaase write all command we have to do:\n\n" +
        "\t\t\tCOMMAND: (ATTENTION, THESE COMMANDS ARE DIFFERENT!)\n\n"
        "\tcode_get-<url> -- Returns the code from your get requests to the url\n" +
        "\tcode_post-<url> -- Returns the code from your post requests to the url\n" +
        "\tbyid-<url>-<id> -- Returns the STATIC HTML element from your get requests to the url by id\n" +
        "\tbytag-<url>-<tag> -- Returns the STATIC HTML element from your get requests to the url by tag\n\n" +
        "\t\tEXAMPLE: code_get-https://stackoverflow.com/ code_post-https://www.google.com/"
        )
        operation = str(input('\tCreate commands:\n\t')).split(" ")
        data = {"scen" : id, "url" : url, "command" : operation}
        print("You want create new case? If yes enter any button, else - \"F\"")
        command = str(input('\t\n'))
        if command == 'F' or command == 'f':
            json.dump(data, file)
            file.write('\n')
            file.write(']')
            file.close()
            work()
        else:
            json.dump(data, file)
            file.write(',\n')
            
    


#READ SCENARION MODEL (PROTOTYPE)
def read(order):
    f_name = order[1]
    file = open(f"{f_name}.json", "r")
    for lines in file:
        print(lines)


#COMMAND N - START 
#STARTS A FUNCTION TREE
def work():
    order = str(input())
    print('\n')
    orderarray = order.split(" ") # Вreaking the request into a command and a URL
    match orderarray[0]: # Getting the operation from the request
        case "-help":
                help()
        case"-code_get":
                p_url = orderarray[1]
                code_get(p_url)
        case"-code_post":
                p_url = orderarray[1]
                code_post(p_url)
        case"-byid":
                p_url = orderarray[1]
                p_id = orderarray[2]
                byid(p_url, p_id)
        case"-bytag":
                p_url = orderarray[1]
                p_tag = orderarray[2]
                bytag(p_url, p_tag)
        case"-byclass":
                p_url = orderarray[1]
                p_class = orderarray[2]
                bytag(p_url, p_class)
        case"-create":
                p_name = orderarray[1]
                create(p_name)
        case _:
                print("\tError\n" + "\tWe're sorry, but this command doesn't exist, please use -help")
                work()




print("\tWelcome, The program is running, enter the command or -help for manual to program\n")
lst = load_workbook('TestResults.xlsx')
if "ScenarioResults" != lst.sheetnames[0]:
    excel()

work()

