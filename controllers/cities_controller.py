from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route('/cities')
def list_all_cities():
    cities = city_repository.select_all()
    return render_template('countries/index.html', all_cities = cities)

#! NEW ROUTE ADDED FOR GETTING CITIES IN COUNTRY BLUEPRINT
@cities_blueprint.route('/countries/show')
def list_cities_by_country(country_name):
    country = country_repository.select(country_name)
    cities = city_repository.select(country)
    return render_template('cities/index.html', all_cities_by_country=cities)

# NEW - DON'T TOUCH
# GET '/cities/new'
@cities_blueprint.route('/cities/new')
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)


# CREATE
# POST '/cities'
@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    new_city_name = request.form['city_name']
    visited = request.form['visited']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(new_city_name, country, visited)
    city_repository.save(city)
    return redirect('/countries')

# SHOW
# GET '/cities/<id>'
@cities_blueprint.route('/cities/<id>', methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('/countries/show.html', city = city)

# EDIT
# GET '/cities/<id>/edit'
@cities_blueprint.route('/cities/<id>/edit', methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template('/cities/edit.html', city = city, all_countries = countries)

# UPDATE
# PUT '/cities/<id>'
@cities_blueprint.route('/cities/<id>', methods=['POST'])
def update_city(id):
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(city_name, country, visited, id)
    city_repository.update(city)
    return redirect('/countries')

# DELETE
# DELETE '/cities/<id>'
@cities_blueprint.route('/cities/<id>/delete', methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/countries/show.html')

