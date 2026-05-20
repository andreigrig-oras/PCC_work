from pathlib import Path
guest=input("Please enter your name:\n")
path=Path('files/guests.txt')
path.write_text(guest)