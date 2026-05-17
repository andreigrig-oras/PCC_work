favourite_places={
    'maria':['canada', 'australia'],
    'mark':['greenland'],
    'joe':['antarctica','new zealand'],
}

for person, place in favourite_places.items():
    if len(place)>1:
        print(f"{person.title()}'s favourite places are:")
        for loc in place:
            print(loc.title())
    else:
        print(f"{person.title()}'s favourite places is {place[0].title()}")