class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant (self):
        print (f"This restaurant is called {self.name} and serves {self.cuisine} food.")
    
    def open_restaurant (self):
        print (f"{self.name} is now open.")

my_restaurant = Restaurant ('Sejour','Indian')
print (f"The {my_restaurant.name} restaurant serves {my_restaurant.cuisine}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant ('Encyclops','futuristic')
their_restaurant = Restaurant ('Myopia', 'small')

your_restaurant.describe_restaurant()
their_restaurant.describe_restaurant()