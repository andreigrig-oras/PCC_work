stop = 5
while stop >= 0:
    age = input ('what is you age?\n')
    age = int(age)
    if age < 3 : print (f"your ticket is free")
    elif age >=3 and age < 12: print (f"the price of your ticket is $10")
    elif age >=12: print (f"the price of your ticket is $15")
    stop -= 1