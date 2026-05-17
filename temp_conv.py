#1st exercise's solution. thoughts?
def convert_temperature(target_scale, temperature=0):
    if target_scale.upper=="F":
        return (temperature*9/5)+32
    elif target_scale.upper=="C":
        return (temperature-32)*5/9
    else: raise "There's been some mistake"
try: a=int(input("Temperature of ... "))
except ValueError as e:
    print (e)
while True:
    b=input("Convert to? C/F")
    if b=="F" or b=="C": break
    else: raise ValueError("Can't do this")
print(convert_temperature(b,a))