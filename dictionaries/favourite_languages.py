favourite_languages = {
    'jen':'rust',
    'mark':'c++',
    'john':'rust',
    'maria':'python',
    'mathew':'c++',
}

names = ['jen','john','andrew','mark','kyle']

for name in names:
    if name in favourite_languages.keys():
        print (f"Thanks for responging {name.title()}\n")
    else: print (f"Take the poll {name.title()}\n")