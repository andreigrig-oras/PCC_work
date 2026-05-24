import matplotlib.pyplot as plt
x_values=range(1,5001)
y_values=[x**3 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values,cmap=plt.cm.Blues)
ax.axis([0,5001, 0,125_000_000_000])
ax.set_title("Cubed numbers",fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("cube of value",fontsize=14)
plt.savefig('cubed_numbers.png')
plt.show()