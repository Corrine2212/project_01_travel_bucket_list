# Project 1: JetSetGo - Travel Bucket List

## Project description:
### What does the application do?
This is my first ever CodeClan project! The brief I chose called for an app that could track someone's travel adventures.
The app had to meet the following criteria:
- app should allow the user to track countries and cities they want to visit and those they have visited.
- app needed to have CRUD functionality:
  - user should be able to create and edit countries
  - each country should have one or more cities to visit
  - the user should be able to create and delete entries for cities
  - the app should allow the user to mark destinations as visited or still to see.

### Technologies used and why?
For the last 4 weeks i've been learning Python, HTML, CSS, Flask framework, Djinja, PostgreSQL, psycopg2 to build a full stack web application. The aim of this project was to consolidate everything that i've learned using the aforementioned languages and framework.

### Challenges faced and features I hope to implement in the future:
Challenges:
  - had imposter syndrome; didn't think I knew what I was doing and didn't know where to even begin.
  - syntax errors
  - not fully understanding how controllers worked 
  - needed to have naming conventions 

For extra functionality/features, I could include:
  - separate pages for destinations visited and those still to visit
  - add sights to the destination cities
  - search for destination by continent, city or country
  - ability to upload pictures and have them displayed as thumbnails
  - extra input fields for notes and date to visit place
  - stats page to see at a glance how many countries you've visited
  - make mobile friendly
  - add comments to explain some of the code

## How to install and run the project:
1. Open files in editor e.g. Visual Studio Code
2. Create database: 'travel_bucket_list.sql' - Run `dropdb travel_bucket_list` then `createdb travel_bucket_list`
3. Run psql in the terminal to initiate the database `psql -d -f travel_bucket_list.sql`
4. Run console.py file using command `python3 console.py`
5. Run Flask using command `flask run`
6. Access webpage using url: http://localhost:4999
7. To exit Flask, use CTRL + C in the terminal 


