import requests
from bs4 import BeautifulSoup
#THIS FILE WAS CREATED AS A COLLECTION OF TEAMS MODELS, 
#THEIR DESCRIPTIONS AND FURTHER DEVELOPMENT

#COMAND 1 - HELP
#THIS COMMAND WILL WRITE A MANUAL FOR USING THE PROGRAM
def help():
    print(
    "This program was created as a website tester, below you can see a list of existing commands:\n\n" +
    "\t-help -- Write a manual for using the program\n" +
    "\t-code -- Returns the code from your get requests to the url\n" +
    "\t-ide -- Returns the HTML element from your get requests to the url by id\n"       
    )
    work()

#COMAND 2 - CODE
#RETURNS THE CODE FROM YOUR GET REQUESTS TO THE URL
def code():
    url = "https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/14-requests.html"
    site = requests.get(url)
    code = site.status_code # CODE OF GET REQUEST
    print("\tReturned сode:" + str(code))
    work()

#COMAND 3 - ELEMENT BY ID
#RETURNS THE HTML ELEMENT FROM YOUR GET REQUESTS TO THE URL BY ID
def byid():
    url = "https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/14-requests.html"
    site = requests.get(url)
    html = site.text # GET HTML OF THE SITE
    search = BeautifulSoup(html, 'html.parser') # PARSING
    u_id = search.find(id='') # ID SEARCH
    print("\tReturned element:" + str(u_id))
    work()

def work():
    order = str(input())
    match order:
        case "-help":
                help()
        case"-code":
                code()
        case"-byid":
                byid()
        case _:
                print("\tError\n" + "\tWe're sorry, but this command doesn't exist, please use -help")
                work()

print("\tWelcome, The program is running, enter the command or -help for manual to program\n")
work()