# this is my solution to exercise 1
multi= lambda x,y: x*y
list_a=[1,2,3,4,5]
b=2
list_b=[multi(x,b) for x in list_a]
print(list_b)

# this is my solution to exercise 2

def decorator (func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

def hw():
    print("Hello World")

hw=decorator(hw)
hw()

# this is my solution to exercise 3

def ctdown(x):
    while x!=0:
        yield x
        x-=1
for i in ctdown(12):
    print(i)

#how did I do?