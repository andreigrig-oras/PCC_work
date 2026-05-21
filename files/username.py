from pathlib import Path
import json

path=Path('files/username.json')

def get_details():
    details={"username":"","first_name":"","last_name":""}
    details['username']=input ("What is your username? ")
    details['first_name']=input ("What is your first name? ")
    details['last_name']=input ("What is your last_name? ")
    content=json.dumps(details)
    path.write_text(content)

def print_details():
    content=path.read_text()
    deets = json.loads (content)
    print(f"Your username is {deets["username"]}")
    print(f"Your first name is {deets["first_name"]}")
    print(f"Your last name is {deets["last_name"]}")

conts=path.read_text()
conti=json.loads(conts)
user_name=conti["username"]

if path.exists():
    check=input("What is your username? ")
    if check == user_name:
        print_details()
    else:
        get_details()
else:    
    get_details()