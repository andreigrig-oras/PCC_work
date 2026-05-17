numbers = range(1, 11)

for number in numbers:
    if number % 2 == 0:  # If the number is even
        continue  # Skip the rest of the loop
    print(number)  # This will print only odd numbers