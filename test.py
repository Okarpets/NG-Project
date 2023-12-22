import json
def find_scen(p_name, p_id):
    with open("{0}.json".format(p_name), "r") as file:
        js_file = json.load(file)
        file.close()
        print("\t\tYour scenario:\n")
        for elem in js_file:
            if str(elem['id']) == p_id:
                print(elem)

    


show("test", "1")