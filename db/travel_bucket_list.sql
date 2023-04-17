DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL,
    visited BOOLEAN DEFAULT FALSE
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255) NOT NULL,
    visited BOOLEAN DEFAULT FALSE,
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
    
);