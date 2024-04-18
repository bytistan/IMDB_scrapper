def read_file(path):
    try:
        with open(path,"r") as file:
            return file.readlines()
    except:
        print("[-] File is not exist")
        return None

import json

def write_json(data,file_name):
    try:
        with open(f"data/{file_name}.json","w") as json_file:
            json_file.write(json.dumps(data))
    except Exception as e:
        print(f"[-] Error : {e}") 
