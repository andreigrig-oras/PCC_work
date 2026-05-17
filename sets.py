bag={1,2,3,4,5,6}
print (bag)
x=1
while x!=0:
    try:
        x=int(input("give me a number to add to the bag, if you want to stop adding stuff, just input 0 ... "))
    except ValueError:
        print("try again")
    bag.add(x)
print(bag)
x=1
while x!=0:
    try:
        x=int(input("Would you like to remove a number? If not input 0 and press enter"))
        try:
            bag.remove(x)
        except KeyError:
            print("already removed")
    except ValueError:
        print("try again")

print(bag)
print (1 in bag)