import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__ (self, num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([1,2,3,4,5,6,7,8,9,10])
        return direction * distance

    def fill_walk (self):
        while len(self.x_values)<self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step==0 and y_step==0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9), dpi=80)
#point_numbers=range(rw.num_points)

ax.plot (rw.x_values,rw.y_values,linewidth=0.8)
ax.scatter(0,0,c='green',edgecolors='none', s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none',s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


ax.set_aspect('equal')
plt.show()