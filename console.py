import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()

# set up variables/objects to pass through
country_1 = Country("Japan", False)
country_repository.save(country_1)

country_2 = Country("Scotland", True)
country_repository.save(country_2)

country_3 = Country("South Korea", False)
country_repository.save(country_3)

country_4 = Country("Denmark", True)
country_repository.save(country_4)


city_1 = City("Tokyo", country_1, False)
city_repository.save(city_1)

city_2 = City("Edinburgh", country_2, False)
city_repository.save(city_2)

city_3 = City("Seoul", country_3, False)
city_repository.save(city_3)

city_4 = City("Osaka", country_1, False)
city_repository.save(city_4)

city_5 = City("Copenhagen", country_4, True)
city_repository.save(city_5)

pdb.set_trace()