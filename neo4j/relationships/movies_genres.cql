LOAD CSV WITH HEADERS FROM 'file:///genres.csv' AS row
MATCH (m:Movie {id: toInteger(row.movie_id)})
MATCH (g:Genre {genre_id: toInteger(row.id)})
CREATE (m)-[:BELONGS_TO]->(g);
