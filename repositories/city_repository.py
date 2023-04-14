from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

# save 
def save(city):
    sql = "INSERT INTO books (city_name, country_id, visited) VALUES (%s, %s, %s,) RETURNING *"
    values = [city.name, city.country.id, city.visited ]
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
        city = City(result['name'], country, result['visited'])
    return city

# select_all
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'])
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
    values = [city.name, city.country.id, city.visited]
    run_sql(sql, values)