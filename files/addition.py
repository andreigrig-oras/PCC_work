print(f"I will be adding two numbers you provide (enter q when you're done):\n")

while True:
    num_1=input("your first number is: ")
    try:
        num_1=int(num_1)
    except ValueError:
        print ("the value you entered is not a number.")
    if num_1 =="q":
        break
    num_2=input("your second number is: ")
    try:
        num_2=int(num_2)
    except ValueError:
        print ("the value you entered is not a number.")
    if num_2 =="q":
        break
    try:
        print (f"{num_1} + {num_2} = {num_1+num_2}")
    except TypeError:
        print ("I cannot add these values")