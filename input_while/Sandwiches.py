sandwiches=['reuben','pastrami','tomato','pastrami','pastrami','tuna']
print ("The deli has ran out of pastrami")
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')
finished_sandwiches=[]
while sandwiches:
    sandwich=sandwiches.pop()
    print (f'I made you a {sandwich} sandwich')
    finished_sandwiches.append(sandwich)

print ('the list of sandwiches that I made you are:')
for sandwich in finished_sandwiches: print(sandwich)