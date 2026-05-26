from random import randint
import plotly.express as px

class Die:
    def __init__ (self, num_sides=8):
        self.num_sides=num_sides
    def roll(self):
        return randint(1, self.num_sides)
    
die_1 = Die ()
die_2 = Die ()
roll_res=[]
for roll_num in range(100000):
    roll_res.append(die_1.roll()+die_2.roll())
max_value=die_1.num_sides+die_2.num_sides
frequencies = []
for value in range(2,max_value+1):
    frequencies.append(roll_res.count(value))
poss_results=range(2,max_value+1)
labels={'x':'Result','y':"Frequency of result"}
fig=px.bar(x=poss_results,y=frequencies,labels=labels)
fig.show()