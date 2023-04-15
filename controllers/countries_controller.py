from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('countries/index.html', all_countries = countries)

# NEW
# GET '/countries/new'
@countries_blueprint.route('/countries/new')
def new_country():
    cities = city_repository.select_all()
    return render_template("countries/new.html", all_cities = cities)


# CREATE
# POST '/countries'
@countries_blueprint.route('/countries', methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    city_id = request.form['city_id']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    country = Country(country_name, city, visited)
    country_repository.save(country)
    return redirect('/countries')

# SHOW
# GET '/countries/<id>'
@countries_blueprint.route('/countries/<id>', methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

# EDIT
# GET '/countries/<id>/edit'
@countries_blueprint.route('/countries/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    return render_template('countries/edit.html', country = country, all_cities = cities)

# UPDATE
# PUT '/countries/<id>'
@countries_blueprint.route('/countries/<id>', methods=['POST'])
def update_country(id):
    country_name = request.form['country_name']
    city_id = request.form['city_id']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    country = Country(country_name, city, visited)
    country_repository.save(country)
    return redirect('/countries')

# DELETE
# DELETE '/countries/<id>'
@countries_blueprint.route('/countries/<id>', methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')
