class Users:
    def __init__ (self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=int(age)
    def greet(self):
        print(f'Dear {self.first_name.title()} {self.last_name.title()}, we welcome you!')

me=Users('andrei','grigoras', '36')
print (f"My first name: {me.first_name.title()}\n")
print (f"My last name: {me.last_name.title()}\n")
print (f"My age: {me.age}\n")

you = Users ('ion', 'creanga', '99')
him = Users ('mihai', 'eminescu', '88')

me.greet()
you.greet()
him.greet()