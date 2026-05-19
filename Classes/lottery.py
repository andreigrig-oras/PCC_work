from random import choice
randos=[1,"a",34,"x",55,"m","b","t",3,23,33,45,19,0,30]
count=4
winning=[]
my_ticket=[34, "b","t",23]
pulls=0


while count!=0:
    lucky = choice (randos)
    randos.remove(lucky)
    if lucky in my_ticket:
        count-=1
    pulls+=1
    print(lucky)
print (f'there have been {pulls} pulls to become a winner')

 #print (f"the following characters are winners: {winning}")