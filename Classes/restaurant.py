class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restaurant (self):
        print (f"This restaurant is called {self.name} and serves {self.cuisine} food.")
    
    def open_restaurant (self):
        print (f"{self.name} is now open.")
    
    def set_number_served (self, new_number):
        self.number_served=new_number

    def increment_number_served (self, additional_number):
        self.number_served+=additional_number

class IceCreamStand (Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ""
    def display_flavors (self):
        print(f"The ice cream stand's flavors are as follows: {self.flavors}\n")

my_shop = IceCreamStand ("Ice Cube", "ice cream")
my_shop.flavors="vanilla, chocolate and pistachio"

my_shop.display_flavors()

#my_restaurant = Restaurant ('Sejour','Indian')

#print(f"My restaurant has served {my_restaurant.number_served} people")

#my_restaurant.number_served = 45
#print(f"My restaurant has served {my_restaurant.number_served} people")

#my_restaurant.set_number_served (35)
#print(f"My restaurant has served {my_restaurant.number_served} people")

#my_restaurant.increment_number_served (200)
#print(f"My restaurant has served {my_restaurant.number_served} people")




#print (f"The {my_restaurant.name} restaurant serves {my_restaurant.cuisine}")
#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()

#your_restaurant = Restaurant ('Encyclops','futuristic')
#their_restaurant = Restaurant ('Myopia', 'small')

#your_restaurant.describe_restaurant()
#their_restaurant.describe_restaurant()