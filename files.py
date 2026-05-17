import json
with open('data.json', 'r') as file:
    data = json.load(file)  # Reads JSON data from a file and converts it to a Python dictionary
    print(data)