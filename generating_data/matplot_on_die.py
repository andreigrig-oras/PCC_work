from random import randint
import matplotlib.pyplot as plt

class Die:
    def __init__ (self, num_sides=8):
        self.num_sides=num_sides
    def roll(self):
        return randint(1, self.num_sides)
    
die_1 = Die ()
die_2 = Die ()

roll_res=[die_1.roll()+die_2.roll() for x in range(10000)]
frequencies = [roll_res.count(value) for value in range(2,die_1.num_sides+die_2.num_sides+1)]

fig, ax = plt.subplots()
max_value=die_1.num_sides+die_2.num_sides
x_values=range(2,max_value+1)
ax.bar(x_values, frequencies)

plt.show()