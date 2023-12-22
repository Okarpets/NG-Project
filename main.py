import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from openpyxl import load_workbook 
from bs4 import BeautifulSoup
import json


#COMMAND USER : 0 - HELP (MAUNAL)
def help():
    print(
    "This program was created as a website tester, below you can see a list of existing commands:\n\n" +
    "\t-help -- Write a manual for using the program\n" +
    "\t-exit -- Exits the program\n" +
    "\t-code_get <url> <json_file OR \"TC\" OR nothing> -- Returns the code from your get requests to the url\n" +
    "\t\t\"TC\" : headers, content, text -- typical commands to return a request (NOT WRITTEN IN EXCEL)\n" +
    "\t-code_post <url> <json_file OR nothing> -- Returns the code from your post requests to the url\n" +
    "\t-byid <url> <id> -- Returns the STATIC HTML element from your get requests to the url by id\n" +
    "\t-bytag <url> <tag> -- Returns the STATIC HTML element from your get requests to the url by tag\n" +
    "\t-create <json_name> -- Create scenario in a document\n" +
    "\t-read <json_name> <id> -- Read and process all scenario in a document OR one scenario in the file by scenario id\n" +
    "\t-show <json_name> <id> -- Show you all scenario in the file OR one scenario in the file by secanrio id\n" +
    "\t\tIf you don't enter id -show test show you all scenarios"
    )
    work()

#COMMAND USER : 1 - RETURN GET CODE REQUESTS (OR ANSWER AFTER PROCESS TYPICAL COMMANDS)
def code_get(orderarray):
    p_url = orderarray[1]
    try:
        if len(orderarray) == 2:
            try:
                site = requests.get(p_url)
            except Exception:
                print("\tInvalid values\n")
                work()
            order = site.status_code # CODE OF GET REQUEST
            print("\tReturned сode: " + str(order) + '\n')
        if len(orderarray) == 3:
            site = requests.get(p_url)   
            match orderarray[2]: # Getting the operation from the request
                case "headers":
                    try:
                        print(site.headers)
                        work()
                    except Exception:
                        err()
                case "text":
                    try:
                        print(site.text)
                        work()
                    except Exception:
                        err()
                case "content":
                    try:
                        print(site.content)
                        work()
                    except Exception:
                        err()
                case _:
                    try:
                        file = open("{}.json".format(orderarray[2]), "r")
                        u_data = json.load(file)
                        site = requests.get(p_url, params=json.dumps(u_data))
                        order = ("The request was processed correctly")
                        print("\tReturned: " + order + '\n')
                    except Exception:
                        order = "Uncorrectly requests"
                        print("\t{0}\n".format(order))
                        work()
    except ConnectionError: 
        print("\tConnection error\n")
    except Timeout:
        print("\tThe request timed out\n")
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['CodeGetResults'] #List in 'TestResult.xlsx'
    xlsx.append([p_url,order]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()

#COMMAND USER : 2 - RETURN POST CODE REQUESTS
def code_post(orderarray):
    try:
        url = orderarray[1]
        if len(orderarray) == 2:
            try:
                site = requests.post(url)
            except Exception:
                print("\tInvalid values\n")
                work()
            order = site.status_code # CODE OF POST REQUEST
            print("\tReturned сode: " + str(order) + '\n')
        if len(orderarray) == 3:
            post = orderarray[2]
            try:
                file = open("{}.json".format(post), "r")
                u_data = json.load(file)
                site = requests.post(url, data=json.dumps(u_data))
            except Exception:
                print("\tUncorrectly requests\n")
                work()
            order = site.status_code # CODE OF POST REQUEST
            print("\tReturned сode: " + str(order) + '\n')
    except ConnectionError: 
        print("\tConnection error\n")
    except Timeout:
        print("\tThe request timed out\n")
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['CodePostResults'] #List in 'TestResult.xlsx'
    xlsx.append([url,order]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()


#COMMAND USER : 3 - RETURN HTML ELEMENT BY ID
def byid(p_url, p_id):
    url = p_url
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    u_id = soup.find_all(id='{0}'.format(p_id))
    print(u_id)
    if u_id == []:
        u_id = "The element ISN'T on the page"
    else:
        u_id = "The element IS on the page"
    print('\t' + u_id + '\n')
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['ElementById'] #List in 'TestResult.xlsx'
    xlsx.append([p_id,url,u_id]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()


#COMMAND USER : 4 - RETURN HTML ELEMENT BY TAG
def bytag(p_url, p_tag):
    url = p_url
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    u_tag = soup.find_all('{0}'.format(p_tag))
    if u_tag == []:
        u_tag = "Tag ISN'T HERE"
        print('\t' + str(u_tag) + '\n')
    else:
        u_tag = "Tag IS here"
    file = 'TestResults.xlsx' #Create or open file with that name
    lst = load_workbook(file) #It is depend on save and close command
    xlsx = lst['ElementByTag'] #List in 'TestResult.xlsx'
    xlsx.append([p_tag,url,u_tag]) #Adding that data in xlsx file
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()
    work()

#COMMAND USER : 5 - CREATE SCENARIO TO JSON FILE
def create(p_name):
    file = open(f"{p_name}.json", 'w')
    file.write('[''\n')
    scen_id = 1
    while True:
        print("\tPlease enter url for {0} scenario: ".format(scen_id))
        url = str(input())
        get = "0" 
        post = "0" 
        htmlid = "0" 
        htmltag = "0"
        get_params = "0"
        post_data = "0"
        oper = "0"
        oper_endp = "0"
        def under_create():
            print(
            "\t\t\tCommand list:\n" +
            "\t\t1 - Get requests\n" +
            "\t\t2 - Post requests\n" +
            "\t\t3 - Element by id\n" +
            "\t\t4 - Element by tag\n\n" +
            "\t\tE - Exit\n" +
            "\t\tC - Go to next scenario"
            )
            order = str(input("\tSelect a command from \"Command list\"\n"))
            return order
        while oper != "end":
            match under_create(): # Getting the operation from the request
                case "1":
                    par_order = str(input("\tDo you want to add params? (Y/ )\n"))
                    if par_order == 'Y' or par_order == 'y':
                        get_params = str(input("\tEnter name of the json-file with params\n"))
                        get = "2"
                    else:
                        get = "1"
                case "2":       
                    par_order = str(input("\tDo you want to add data? (Y/ )\n"))
                    if par_order == 'Y' or par_order == 'y':
                        post_data = str(input("\tEnter name of the json-file with data\n"))
                        post = "2"
                    else:
                        post = "1"
                case "3":                   
                    htmlid = str(input("\tEnter HTML elemnent id\n"))                       
                case "4":                            
                    htmltag = str(input("\tEnter HTML elemnent tag\n"))
                case "E":
                    json.dump(data, file)
                    file.write('\n'']')
                    file.close()
                    oper = "end"      
                    oper_endp = "end"
                case "C":
                    if get == "0" and post == "0" and htmlid == "0" and htmltag == "0":
                        print("The scenario will not be added because it is empty")
                    else:
                        json.dump(data, file)
                        file.write(',\n')
                        scen_id += 1
                        oper = "end"
                case _:
                    print("This command doesn't exist, use \"Command list\"")
            data = {"id" : scen_id, "url" : url, "get" : get, "params" : get_params, "post" : post, "data" : post_data, "htmlid" : htmlid, "htmltag" : htmltag}
        if oper_endp == "end":
            break
            
#COMMAND USER : 6 - COMMAND TO CREATE REQUESTS FOR SCENARIO PROCESSING IN AN EXCEL FILE
def read(p_name, p_id):
    if p_id == "0":
        file = open("{0}.json".format(p_name), "r")
        file = json.load(file) 
        for lines in file:
            handle(lines, p_name)
        print("\n\t\tAll the scenario was processed\n")
    else:  
        with open("{0}.json".format(p_name), "r") as file:
            js_file = json.load(file)
            file.close()
            for elem in js_file:
                if str(elem['id']) == str(p_id):
                    handle(elem, p_name)
        print("\n\tScenario was processed\n")
    work()


#COMMAND USER : 7 - SHOW ALL THE FILE OF SCENARIO
def show(p_name, p_id):
    with open("{0}.json".format(p_name), "r") as file:
        if p_id == "0":
            print("\t\tYour scenario:\n")
            for lines in file:
                print(lines)
            file.close()
            work()
        js_file = json.load(file)
        file.close()
        print("\t\tYour scenario:\n")
        for lines in js_file:
            if str(lines['id']) == str(p_id):
                print(lines)
                work()
        print("Scenario with that id wasn't found or it doesn't exist")
        work()


#TECHNICAL COMMANDS NOT USER APPLICABLE
############################################################################
    
#COMMAND ANSWER : 1 - FORMATS .XLSX DOCUMENT
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
    lst.create_sheet('ElementByTag')
    lst['CodeGetResults'].append(["Url","Order"])
    lst['CodePostResults'].append(["Url","Order"])
    lst['ElementById'].append(["Given Id","Url","Result"])
    lst['ElementByTag'].append(["Given Tag","Url","Result"])
    lst['ScenarioResults'].append(["Scenario ID","Url","Get requests", "Post requests", "Find-order by id","Find-order by tag", "Scenario-file name"])
    lst.save(file) #REMEMBER THE WRITING RULES
    lst.close()


#COMMAND ANSWER : 2 - ERROR MESSAGES
def err():
    print("\t\tInvalid value\n\tTry again or use -help for help\n")
    work()


#COMMAND ANSWER : 3 - PROCESS SCENARIOS
def handle(lines, p_name):
        scen_id = lines['id']
        url = lines['url']
        code_get = lines['get']
        get_params = lines['params']
        code_post = lines['post']
        post_data = lines['data']
        u_id = lines['htmlid']
        u_tag = lines['htmltag']

        #GET PART
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

        #POST PART
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

        #ID PART
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
        
        #TAG PART
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
############################################################################
    

#COMMAND MAIN - START 
#STARTS A FUNCTION TREE
def work():
    order = str(input('\n'))
    orderarray = order.split(" ") # Вreaking the request into a command and a URL
    match orderarray[0]: # Getting the operation from the request
        case"-help":
                try:
                    help()
                except Exception:
                    err()
        case"-exit":
                print("\t\tExit the program")
                return 0
        case"-code_get":
                code_get(orderarray)
        case"-code_post":
                code_post(orderarray)
        case"-byid":
                try:
                    p_url = orderarray[1]
                    p_id = orderarray[2]
                    byid(p_url, p_id)
                except Exception:
                    err()
        case"-bytag":
                try:
                    p_url = orderarray[1]
                    p_tag = orderarray[2]
                    bytag(p_url, p_tag)
                except Exception:
                    err()
        case"-create":
                try:
                    p_name = orderarray[1]
                    create(p_name)
                except Exception:
                    err()
        case"-read":
                try:
                    if len(orderarray) == 2:
                        p_name = orderarray[1]
                        read(p_name, "0")
                    if len(orderarray) == 3:
                        p_name = orderarray[1]
                        p_id = orderarray[2]
                        read(p_name, p_id)
                except Exception:
                    err()
        case"-show":
                try:
                    if len(orderarray) == 2:
                        p_name = orderarray[1]
                        show(p_name, "0")
                    if len(orderarray) == 3:
                        p_name = orderarray[1]
                        p_id = orderarray[2]
                        show(p_name, p_id)
                except Exception:
                    err()
        case _:
                print("\tError\n" + "\tWe're sorry, but this command doesn't exist, please use -help")
                work()


#MAIN !!!
print("\tWelcome, The program is running, enter the command or -help for manual to program\n")
lst = load_workbook('TestResults.xlsx')
if "ScenarioResults" != lst.sheetnames[0]:
    excel()

work()