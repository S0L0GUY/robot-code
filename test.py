import json
import os

while True:
    while True:
        try:
            with open('json_files/controller_inputs.json', 'r') as file:
                data = json.load(file)
            
            break
        except:
            pass

    os.system('cls')
    print(json.dumps(data, indent=4))