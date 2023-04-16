class Country:
    def __init__(self, country_name, id = None):
        self.country_name = country_name
        self.id = id

    # def get_cities(self):
    #     return [city for city in all_cities if city.country == self]