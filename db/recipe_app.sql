DROP TABLE IF EXIST recipes;

CREATE TABLE recipes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    ingredients TEXT,
    instructions TEXT,
    author VARCHAR(255),
    category VARCHAR(255),
    cooking_time INT,
    difficulty INT
);
