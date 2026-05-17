number = input ("please provide a number to analyze: ")
number=int(number)
if number % 10 == 0 :
    print (f'{number} is 10 or a multiple of 10')
else: print (f'your number, {number}, is not a multiple of 10')