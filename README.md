# Si'test application

 A console application created to work with site requests and their HTML structures using scenarios or monofunctions. The results are written to an excel file called TestResults.


## Monofunctions

- `-help` - Write a manual for using the program

- `-exit` - Exits the program

- `-code_get <url>` - Returns the code from your get requests to the url

- `-code_post <url> <json_file name/without>` - Returns the code from your post requests to the url

- `-byid <url> <id>` - Returns the STATIC HTML element from your get requests to the url by id

- `-bytag <url> <tag>` - Returns the STATIC HTML element from your get requests to the url by tag

- `-show <json_name>` - Show you all scenario in the file

## Functions for interacting with scenarios

- `-create <json_name>` - Create scenario in a document

- `-read <json_name>` - Read and process all scenario in a document

## How to use
**1.** Create excel file called *"TestResults"*.  
**2.** Start *"main.py"* and Open the console and write `pip install -r requirements.txt`  
**3.** Run and use.

## Requirements

All scenarios are accepted in json format, if you don't want to write them manually use `-create <json_name>` to create scenarios. In case you want to create them yourself, they must correspond to this structure:

```bash
  [
  {"url": "https://text.ru/", "get": "1", "post": "1", "htmlid": "master-menu", "htmltag": "0"},
  {"url": "https://ecostyle.ua/pay/login.php?account=&phone=", "get": "0", "post": "0", "htmlid": "contact-form-7-js-extra", "htmltag": "div"}
  ]
```

Operations in which there is no additional data take the form 0 or 1, if they need to be done during the `-read <json_name>` command, then you need to set 1, but if processing of this command is not needed, use 0. For example, in the first line commands are processed: `-code_get`, `-code_post`, `-byid <url> <id>` and command `-bytag <url> <tag>` - aren't processed.

## If you notice a bug or critical error
### Contact information for feedback****
Gmail: karpetsolekasandrschool10@gmail.com		
GitHub: https://github.com/Okarpets/
