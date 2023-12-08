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










# SHOW ALL THE FILE
def json_show(name):
    with open("{0}.json".format(name), "r") as file:
        for elem in file:
            print(elem)
    file.close()


# FUNCTION TEST
name = str(input())
json_show(name)
