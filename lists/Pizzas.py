pizzas=["pepperoni", "hawaian", "neapolitan"]
#for pizza in pizzas:
#    print(f"I enjoy {pizza} pizza!")
#print("Isn't pizza great!\n")

print (pizzas[-2:])
friend_pizzas=pizzas[:]
pizzas.append("macaroni")
friend_pizzas.append("omlette")
print (f"my pizzas:")
for pizza in pizzas: print (pizza)
print (f"\nmy friend's pizzas:")
for pizza in friend_pizzas: print (pizza)