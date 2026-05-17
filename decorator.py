def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")
def say_bye():
    pass
say_bye = my_decorator(say_hello)
say_hello()
say_bye()