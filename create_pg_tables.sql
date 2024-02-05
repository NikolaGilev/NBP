DROP TABLE IF EXISTS collections, genres, movies, "cast", crew, keywords;

CREATE TABLE collections (
    pkey SERIAL PRIMARY KEY,
	id INT,
    name VARCHAR(255) NOT NULL,
	poster_path VARCHAR(255),
	backdrop_path VARCHAR(255),
    movie_id INT
);

CREATE TABLE genres (
    pkey SERIAL PRIMARY KEY,
	id INT,
    name VARCHAR(255) NOT NULL,
    movie_id INT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    imdb_id VARCHAR(20) ,
    title VARCHAR(255) ,
    for_adults BOOLEAN,
    budget BIGINT,
    original_language VARCHAR(10) ,
    original_title VARCHAR(255) ,
    overview TEXT,
    popularity FLOAT,
    release_date DATE,
    revenue FLOAT,
    runtime FLOAT
);

CREATE TABLE "cast" (
	pkey SERIAL PRIMARY KEY, 
    id INT,
	profile_path VARCHAR(255),
	credit_id VARCHAR(255),
	cast_id VARCHAR(255),
    movie_id INT,
    name VARCHAR(255) NOT NULL,
    character VARCHAR(512),
    gender INT
);


CREATE TABLE crew (
    pkey SERIAL PRIMARY KEY,
	id INT,
    movie_id INT,
	credit_id VARCHAR(255),
    department VARCHAR(255),
    job VARCHAR(255),
    gender VARCHAR(255),
	profile_path VARCHAR(255),
    name VARCHAR(255)
);

CREATE TABLE keywords (
	pkey SERIAL PRIMARY KEY,
    id INT,
    name VARCHAR(255),
    movie_id INT
);

