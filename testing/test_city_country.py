from city_country import city_country
def test_city_country():
    test_name=city_country("buenos aires","argentina")
    assert test_name== "Buenos Aires, Argentina"
def test_city_country_popultation():
    test_name=city_country("buenos aires","argentina", "1000000")
    assert test_name== "Buenos Aires, Argentina -- population: 1000000"