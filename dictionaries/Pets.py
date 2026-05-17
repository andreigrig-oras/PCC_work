pet1 = {
    'animal':'cat',
    'person':'maria',
}
pet2 = {
    'animal':'dog',
    'person':'mark',
}
pet3 = {
    'animal':'turtle',
    'person':'ben',
}
pets=[pet1,pet2,pet3]
for pet in pets:
    print(f"{pet['person'].title()} owns a {pet['animal']}.")