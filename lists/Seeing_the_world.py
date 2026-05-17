places=['Japan','Sweden','Ireland','Iceland','China']
print(places) #printing the list in it's original form
print(sorted(places)) #printing list in alphabetical order without modifying original
print(places) #showing the list remains in the same order
rev_places=sorted(places)
rev_places.reverse()
print(rev_places) # reverse alphabetical witohut changing original list
print(places) #showing original list is in right order
places.reverse()
print(f"reversed list now: {places}")
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print (places)