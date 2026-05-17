car="bmw"
print(f"is car =='bmw'?, I predict True")
print(car=="bmw")
print(f"is car =='audi'?, I predict False")
print(car=="audi")
print(f"is car !='audi'?, I predict True")
print(car!="audi")

age=20
print(f"is age == 21?, I predict False")
print(age==21)
print(f"is age != 21?, I predict True")
print(age!=21)
print(f"is age >= 21?, I predict False")
print(age>=21)
print(f"is age <= 21?, I predict True")
print(age<=21)

cars=["audi","bmw","mercedes"]
if "audi" in cars and "bmw" in cars and "bike" not in cars:
    print("Audi and BMW are cars, but bikes aren't cars")