from pathlib import Path
guest=''
path=Path('files/guests.txt')
guest_list=""
while guest!="Done":
    guest=input("Please enter your name (if you're done inputting names, write Done and press enter):\n")
    if guest == "Done:":
        break
    else:
        guest_list+= f"{guest}\n"
path.write_text(guest_list)