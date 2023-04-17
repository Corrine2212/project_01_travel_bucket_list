class Country:
    def __init__(self, country_name, visited = False, id = None):
        self.country_name = country_name
        self.visited = visited
        self.id = id

    # def get_cities(self):
    #     return [city for city in all_cities if city.country == self]

    def mark_visited(self):
        self.visited = True