DROP DATABASE IF EXISTS vehicles; 
CREATE DATABASE vehicles; 

\c vehicles

CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY, 
    car_type TEXT NOT NULL, 
    car_brand TEXT NOT NULL, 
    car_price FLOAT NOT NULL, 
    car_rating INT NOT NULL, 
    car_is_eco_friendly BOOLEAN NOT NULL
);

INSERT INTO cars (car_type, car_brand, car_price, car_rating, car_is_eco_friendly)
VALUES
    ('Saloon', 'Mercedez-Benz', 50000, 8, FALSE), 
    ('4 x 4', 'Toyota', 25000, 6, TRUE), 
    ('Offroad', 'Honda', 40000, 9, FALSE)
RETURNING *;