from pathlib import Path
import json

path=Path('files/fav_num.json')

def red_num():
    content=path.read_text()
    fav_num = json.loads (content)
    print(f"Your favorite number is {fav_num}")

#red_num()