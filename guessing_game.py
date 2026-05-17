#My solution to exercise 5, what do you think?
import random
y=random.randint(1,101)
z=1
print("Guess the number I'm thinking of between 1-100 ... (attempt 1) ")
while True:
    z+=1
    try:
        x=int(input())
        if x<y: print(f"too low, guess higher (attempt {z}) ... ")
        elif x>y: print(f"too high, guess lower (attempt {z}) ... ")
        else:
            print(f"congrats, you guessed the number is {y}, it only took you {z-1} tries")
            break
    except ValueError: print("That's no number bro, try again ...")