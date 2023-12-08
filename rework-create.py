import json
#COMMAND 6 - CREATE SCENARIO MODEL
def create(a):
    file = open(f"{a}.json", 'w')
    file.write('[''\n')
    command = "0"
    while True:
        id = str(input('\tEnter scenario id: '))
        url = str(input('\tEnter url: '))
        print(
            "\t\t\tNow pleaase write all command we have to do:\n\n" +
        "\t\t\tCOMMAND: (ATTENTION, THESE COMMANDS ARE DIFFERENT!)\n\n"
        "\tcode_get -- Returns the code from your get requests to the url\n" +
        "\tcode_post -- Returns the code from your post requests to the url\n" +
        "\tbyid-<id> -- Returns the STATIC HTML element from your get requests to the url by id\n" +
        "\tbytag-<tag> -- Returns the STATIC HTML element from your get requests to the url by tag\n\n" +
        "\t\tEXAMPLES: code_get-https://stackoverflow.com/ code_post-https://www.google.com/"
        )
        operation = (str(input('\tCreate commands:\n\t')).replace(" ",", ")).replace("-", " : ")
        print(operation)
        data = {"scen" : id, "url" : url, "operation" : operation}
        print("\n\t\tYou want create new case? If yes enter any button, else - \"F\"")
        command = (input('\t\n'))
        if command == 'F' or command == 'f':
            json.dump(data, file)
            file.write('\n')
            file.write(']')
            file.close()
            work()
        else:
            json.dump(data, file)
            file.write(',\n')

def work():
    a = str(input())
    create(a)

work()