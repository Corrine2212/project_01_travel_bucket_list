from db.run_sql import run_sql

from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

# save 
def save(city):
    sql = "INSERT INTO cities (city_name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.city_name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

# select 
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['city_name'], country, result['visited'], result['id'])
    return city

# select_all
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

# delete
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# delete_all
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

# update
def update(city):
    sql = "UPDATE cities SET (city_name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.city_name, city.country.id, city.visited, city.id]
    run_sql(sql, values)


def cities_by_country(country):
    cities = []

    sql = "SELECT * FROM countries WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['city_name'], country, row['visited'], row['id'])
        cities.append(city)
        return cities