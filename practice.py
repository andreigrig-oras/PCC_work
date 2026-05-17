# You gave me the following exercises previously, can you tell me how I can improve?
# Exercise 3 - Part A:
# Write a function sum_numbers(*args) that returns the sum of all numbers passed to it
# The function should be able to accept any number of arguments.

def sum_numbers(*args):
    sum=0
    for arg in args:
        sum+=arg
    return sum
x=sum_numbers(1,2,3,4,5)
print (f"your sum is {x}")

# Exercise 3 - Part B:
# Create a function describe_city(**kwargs) that takes city attributes (such as name, country, population) as keyword arguments
# and prints a summary sentence using these attributes.

def describe_city(**kwargs):
    return kwargs
a_city={describe_city(name="New York", population= 20, country="USA")}
city_name= a_city.values(name)
print (f"In the city of {a_city.value{name}}")