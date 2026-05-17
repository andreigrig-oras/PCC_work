vacations={}
while True:
    name = input ("What's your name: ")
    vacation = input ("What's your dream vacation: ")
    vacations[name]=vacation
    another = input ("Would you like to add more people to the list (yes/no): ")
    if another == "no": break
print ("Poll completed, here are the findings:")
for name, vacation in vacations.items():
    print (f'{name.title()} would like to go to {vacation.title()}')