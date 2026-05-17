person0 = {'f_name':'mark','l_name':'stevens','age':45,'city':'new york'}
#print (person['f_name'].title())
#print (person['l_name'].title())
#print (person['age'])
#print (person['city'].title())

person1 = {'f_name':'kim','l_name':'jong','age':53,'city':'pyong yang'}
person2 = {'f_name':'tony','l_name':'colette','age':30,'city':'adelaide'}

people=[person0,person1,person2]

for person in people:
    print (f'name:{person['f_name'].title()} {person['l_name'].title() }')
    print (f'age: {person['age']}')
    print (f'city {person['city'].title()}\n')