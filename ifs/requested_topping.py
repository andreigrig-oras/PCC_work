requested_toppings = ['mushrooms','green peppers','extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping== "mushrooms": print ("Ran out of mushrooms, bruv")
        else: print (f"We have added {requested_topping} to your pizza")
    print(f"Your pizza is complete!")
else: print ("Are you sure you want a plain pizza")