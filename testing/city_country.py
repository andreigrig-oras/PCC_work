
def city_country (city, country, population=""):
    if population != "":
        formatted_name = f"{city.title()}, {country.title()} -- population: {population}"
    else:
        formatted_name = f"{city.title()}, {country.title()}"
    return formatted_name
#test_city=input("tell me the name of a city: ")
#test_country=input("in which country is this city located? ")
#test_name=city_country(test_city,test_country)
#print(test_name)