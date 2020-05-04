CREATE TABLE flights(
    id SERIAL PRIMARY KEY,#Every flight has an unique id
    origin VARCHAR NOT NULL, #Other columns just text, notnull so not empty
    destination VARCHAR NOT NULL, 
    duration INTEGER NOT NULL
);