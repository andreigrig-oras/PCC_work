#exercise 4
while True:
    try:
        x=int(input("Input a number ... "))
        break
    except ValueError: print("That is not a numerical value")
print (f"Thanks for entering the number {x}")