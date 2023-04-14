class Country:
    def __init__(self, country_name, visited = False id = None) -> None:
        self.country_name = country_name
        self.visited = visited
        self.id = id