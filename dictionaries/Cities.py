cities = {
    'chicago':['usa', 4.5, 'windy city'],
    'london':['uk',20,'thames'],
    'paris':['france',15.2,'napoleon'],
}
for name, details in cities.items():
    print (f"the city of {name} is located in {details[0].title()}, it's population is {details[1]} thousand people, and it's called {details[2].title()}")