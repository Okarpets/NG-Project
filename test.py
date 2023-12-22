import json
import requests


#match orderarray[2]: # Getting the operation from the request
#                case "headers":
#                    try:
#                        print(site.headers)
#                        work()
#                    except Exception:
 #                       err()
  #              case "text":
    #                try:
   #                     print(site.text)
     #                   work()
      #              except Exception:
       #                 err()
        #        case "content":
         #           try:
          #              print(site.content)
           #             work()
            #        except Exception:
             #           err()
              #  case _:


 


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

                case "F":

                    json.dump(data, file)
                    file.write('\n'']')
                    file.close()
                    oper = "end"      
                    oper_endp = "end"
                case "C":

                    json.dump(data, file)
                    file.write(',\n')
                    scen_id += 1
                    oper = "end"
                    print("\tPlease enter url for {0} scenario: ".format(scen_id))
                
                case _:
                    print("This command doesn't exist, use \"Command list\"")
                    
            data = {"id" : scen_id, "url" : url, "get" : get, "params" : get_params, "post" : post, "data" : post_data, "htmlid" : htmlid, "htmltag" : htmltag}
        if oper_endp == "end":
            break


create("testy")









#SCENREAD




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
