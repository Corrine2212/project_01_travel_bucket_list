import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()

# set up variables/objects to pass through

pdb.set_trace()