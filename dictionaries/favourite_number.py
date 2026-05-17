fav_num={
    "mark":[45,33,21],
    "mike":[22],
    "moop":[12,24],
    "nana":[3,456,67],
         }
for name, numbers in fav_num.items():
    print (f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print (number)
