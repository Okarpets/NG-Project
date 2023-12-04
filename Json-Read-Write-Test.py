import json
from jsonpath_ng import parse

# ADD OR CREATE SCENARIO IN THE FILE
def json_add(scen_num, t_url, t_code):
    userdata = {"scenario{0}".format(scen_num) : { "url" : t_url, "code" : t_code }}
    userdata = json.dumps(userdata)
    userdata = json.loads(str(userdata))
    with open("scenario.json", "w") as file:
        json.dump(userdata, file, indent = 4)
        file.close()

# SHOW ALL THE FILE
def json_show():
    with open("scenario.json", "r") as file:
        for elem in file:
            print(elem)
    file.close()

# SHOW JSON DETAIL
def json_detail(element_order):
    with open("scenario.json", "r") as file:
        result = [m.value for m in parse('$..{}'.format(element_order)).find(json.loads(file.read()))]
        #Parising user order and find it on that json file
        for element_order in (result):
            print(result)


# FUNCTION TEST
scen_num = "3"
t_url = "https://linuxusers.com"
t_code = "300"
element_order = "code"
json_add(scen_num,t_url,t_code)
json_show()
json_detail(element_order)





