from two_d8s import Die
import plotly.express as px

die1=Die()
die2=Die()
die3=Die()

roll_res=[]
for roll_num in range(100000):
    roll_res.append(die1.roll()+die2.roll()+die3.roll())

max_value=die1.num_sides+die2.num_sides+die3.num_sides
frequencies=[]
for value in range(3,max_value):
    frequencies.append(roll_res.count(value))

poss_results=range(3,max_value)
fig=px.bar(x=poss_results, y=frequencies)
fig.show()