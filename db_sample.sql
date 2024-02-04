CREATE TABLE collections (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    movie_id INT
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    movie_id INT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    imdb_id VARCHAR(20) NOT NULL,
    title VARCHAR(255) NOT NULL,
    for_adults BOOLEAN,
    collections_id INT, -- ??
    budget BIGINT,
    original_language VARCHAR(10) NOT NULL,
    original_title VARCHAR(255) NOT NULL,
    overview TEXT,
    popularity BIGINT,
    release_date DATE,
    revenue BIGINT,
    runtime FLOAT
);

CREATE TABLE "cast" (
    id SERIAL PRIMARY KEY,
	credit_id VARCHAR(255),
	cast_id VARCHAR(255),
    movie_id INT,
    name VARCHAR(255) NOT NULL,
    character VARCHAR(255) NOT NULL,
    gender INT
);


CREATE TABLE crew (
    id SERIAL PRIMARY KEY,
    movie_id INT,
    department VARCHAR(255) NOT NULL,
    job VARCHAR(255) NOT NULL,
    gender VARCHAR(255),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE keywords (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    movie_id INT
);

