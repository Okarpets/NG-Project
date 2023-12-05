import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
#THIS FILE WAS CREATED AS A COLLECTION OF TEAMS MODELS, 
#THEIR DESCRIPTIONS AND FURTHER DEVELOPMENT

#COMAND 0 - HELP
#THIS COMMAND WILL WRITE A MANUAL FOR USING THE PROGRAM
def help():
    print(
    "This program was created as a website tester, below you can see a list of existing commands:\n\n" +
    "\t-help -- Write a manual for using the program\n" +
    "\t-code <url> -- Returns the code from your get requests to the url\n" +
    "\t-byid <url> <id> -- Returns the HTML element from your get requests to the url by id\n"       
    )
    work()

#COMAND 1 - CODE_GET
#RETURNS THE CODE FROM YOUR GET REQUESTS TO THE URL
def code_get(p_url):
    try:
        url = p_url
        site = requests.get(url)
        code = site.status_code # CODE OF GET REQUEST
        print("\tReturned сode: " + str(code))
    except ConnectionError: 
        print("\tConnection error\n")
    except Timeout:
        print("\tThe request timed out\n")

    work()
#COMAND 2 - CODE_POST
#RETURNS THE CODE FROM YOUR POST REQUESTS TO THE URL
def code_post(p_url):
    try:
        url = p_url
        site = requests.post(url)
        code = site.status_code # CODE OF POST REQUEST
        print("\tReturned сode: " + str(code))
    except ConnectionError: 
        print("\tConnection error\n")
    except Timeout:
        print("\tThe request timed out\n")

    work()


#COMAND 3 - ELEMENT BY ID
#RETURNS THE HTML ELEMENT FROM YOUR GET REQUESTS TO THE URL BY ID
def byid(p_url, p_id):
    url = p_url
    site = requests.get(url)
    html = site.text # GET HTML OF THE SITE
    u_id = "id=\"{}\"".format(p_id) # ID SEARCH
    if u_id in html:
        print("\tThe element IS on the page\n")
    else:
        print("\tThe element ISN'T on the page\n")
    work()

def work():
    order = str(input())
    orderarray = order.split(" ") # Вreaking the request into a command and a URL
    print(orderarray)
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
        case _:
                print("\tError\n" + "\tWe're sorry, but this command doesn't exist, please use -help")
                work()

print("\tWelcome, The program is running, enter the command or -help for manual to program\n")
work()
