from random import randint
class Die:
    def __init__ (self, sides=6):
        self.sides=sides
    def roll_die(self, count=10):
        while count!=0:
            print(f"you rolled a {randint(1,self.sides)}")
            count-=1

print ("six sided 10 times")
six_sided=Die()
six_sided.roll_die()

print("10 sided twice")
ten_sided=Die(10)
six_sided.roll_die(2)

print ("20 sided three times")
twenty_sided=Die(20)
twenty_sided.roll_die(3)