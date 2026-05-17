rivers={
    'nile':"egypt",
    'amazon':'brazil',
    'yangtze':'china',
    'mississippi':'usa',
    'ganges':'india',
        }

for river, country in rivers.items():
    if country != 'usa':
        print (f'The {river.title()} goes through {country.title()}')
    else:
        print (f'The {river.title()} goes through the {country.upper()}')

for river in rivers:
    print (river.title())

for country in rivers.values():
    if country != 'usa':
        print (country.title())
    else:
        print (country.upper())