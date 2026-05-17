#How did I do?
def divide(x, y):
    try: return x/y
    except ZeroDivisionError: print ("Can't divide by 0")
    finally: print (f"You have attempted to divide {x} by {y}, nice!")
a= int(input ("What number would you like to divide? "))
b= int(input (f"And what number would you like to divide {a} by? "))
c=divide(a,b)
print (f"Your result is {c}")