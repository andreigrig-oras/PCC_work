from pathlib import Path
import json
from read_fav_num import red_num

path=Path('files/fav_num.json')

def get_number():
    num=input ("What is your favorite number? ")
    f_num=json.dumps(num)
    path.write_text(f_num)

if path.exists():
    red_num()
else:    
    get_number()