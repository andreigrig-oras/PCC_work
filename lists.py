list=["c","b","a","d","e","f","g"]
list2=[]
v=3
x=len (list)
while x!=0:
        print ("Number ", len(list)-x+1, " on the list is ", list[len(list)-x])
        x-=1
while v!=0:
    a=int(input("let's slice the list between position ... "))
    b=int(input("and ... "))
    list2=list[a:b]
    x=len(list2)
    while x!=0:
        print ("Number ", len(list2)-x+1, " on the list is ", list2[len(list2)-x])
        x-=1
    v=0