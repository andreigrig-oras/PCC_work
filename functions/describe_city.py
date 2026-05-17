def describe_city (name, country='iceland'):
    print (f'{name.title()} is located in {country.title()}')
describe_city ('Geneva','Switzerland')
describe_city ('Reykjavik')
describe_city(country='texas',name='houston')