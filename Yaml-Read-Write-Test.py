import yaml

# Fucntion of creation/writing yaml file
def yaml_add(scen_num, t_url, t_code): 
    with open('scenario.yaml', 'w') as yaml_file:
        userdata = """
        url: {1}
        code: {2} 
        scen{0}:
        """.format (scen_num, t_url, t_code)
        check_data_load = yaml.safe_load(userdata)
        yaml.dump(check_data_load, yaml_file)
        print("That your scenario, you sure?")
        print(open('scenario.yaml').read())

scen_num = "1"
t_url = "3"
t_code = "4"
yaml_add(scen_num, t_url, t_code) # Add user scenario to yaml file


def yaml_read():
    with open('scenario.yaml', 'r') as file:
        docs = yaml.safe_load_all(file)
        for doc in docs:
            print(doc)


          

yaml_read()




