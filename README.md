# Si'test application

 A console application created to work with site requests and their HTML structures using scenarios or monofunctions. The results are written to an excel file called TestResults.


## Monofunctions

- `-help` - Write a manual for using the program

- `-exit` - End program execution

- `replace <new-xlsx-file name>` - Allows you to change the current Excel file for writing

- `-code_get <url> <json_file OR typical command OR nothing>` - Returns the code from your get requests to the url
 
 `TC : headers, content, text -- typical commands to return a request (NOT WRITTEN IN EXCEL)`

- `-code_post <url> <json_file OR nothing>` - Returns the code from your post requests to the url

- `-byid <url> <id>` - Returns the STATIC HTML element from your get requests to the url by id

- `-bytag <url> <tag>` - Returns the STATIC HTML element from your get requests to the url by tag

- `-show <json_name>` - Show you all scenario in the file

## Functions for interacting with scenarios

- `-create <json_name>` - Create scenario in a document

- `-process <json_name> <id>` - Process all scenario in a document OR one scenario in the file by scenario id

- `-show <json_name> <id>` -- Show you all scenario in the file OR one scenario in the file by scenaio id

 `If you don't enter an id in -show, all scenarios will be shown to you`

## How to use
**1.** Create excel file called *"TestResults"*.  
**2.** Start *"main.py"* and Open the console and write `pip install -r requirements.txt`  
**3.** Run and use.

## Requirements

All scenarios are accepted in json format, if you don't want to write them manually use `-create <json_name>` to create scenarios. In case you want to create them yourself, they must correspond to this structure:

```bash
    [
    {"id": 1, "url": "https://dada.com.ua/", "get": "1", "params": "0", "post": "1", "data": "0", "htmlid": "op-er-t", "htmltag": "p"},
    {"id": 2, "url": "https://elit-ampir.com.ua/ua/p1212509987-molding-home-decor.html", "get": "0", "params": "0", "post": "0", "data": "0", "htmlid": "tr-op", "htmltag": "a"},
    .
    .
    .
    {"id": N, "url": "https://www.youtube.com/watch?v=HfBJ0_1c4PU", "get": "1", "params": "0", "post": "0", "data": "0", "htmlid": "0", "htmltag": "div"}
    ]
```

Operations in which there is no additional data take the form 0 or 1, if they need to be done during the `-read <json_name>` command, then you need to set 1, but if processing of this command is not needed, use 0. For example, in the first line commands are processed: `-code_get`, `-code_post`, `-byid <url> <id>` and command `-bytag <url> <tag>` - aren't processed.

