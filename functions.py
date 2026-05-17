#Here you go, how did I do?
def calculate_area (x,y):
    return x*y
while True:
    try:
        a= int(input("What is the length of your rectangle? (in cm) "))
        b= int(input("What is the width of your rectangle? (in cm) "))
        break
    except ValueError:
        print("Please try using numbers")
print(f"I guess the area of your rectangle is {calculate_area(a,b)}")