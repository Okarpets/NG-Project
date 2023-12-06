#CREATE SCENARIO MODEL (PROTOTYPE)
def create(order):
    f_name = order[1]
    file = open(f"{f_name}.json", "w")
    file.write("Your scenario")
    print("You want create new case? If yes enter any button, else - \"F\"")
    command = str(input())
    if command == 'F' or command == 'f':
        file.close()
    else:
        print("Fill out")
        create(order)


#READ SCENARION MODEL (PROTOTYPE)
def read(order):
    f_name = order[1]
    file = open(f"{f_name}.json", "r")
    for lines in file:
        print(lines)


order = "-read dumps".split(" ")
read(order)

#    -byid https://requests.readthedocs.io/projects/requests-html/en/latest/ goog-gt-tt