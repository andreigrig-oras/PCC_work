#Solution to 4th exercise
bag1={1}
bag2={3}
for i in range(1,6): bag1.add(i)
for i in range(3,8): bag2.add(i)
print ("Bag1= ", bag1, "and bag2= ", bag2)
#Find the union, intersection, difference, and symmetric difference of the two sets.
union_bag=bag1.union(bag2)
intersection_bag=bag1.intersection(bag2)
difference_bag=bag1.difference(bag2)
symmetric_bag=bag1.symmetric_difference(bag2)
#Check if the number 6 is present in each set.
print (6 in bag1)
print (6 in bag2)
#Add the number 8 to both sets.
bag1.add(8)
bag2.add(8)
#Print the length of each set.
print(len(bag1),len(bag2))