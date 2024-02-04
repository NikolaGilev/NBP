LOAD CSV WITH HEADERS FROM 'file:///cast.csv' AS row
MATCH (m:Movie {id: toInteger(row.movie_id)})
MATCH (a:Cast {actor_id: toInteger(row.id)})
CREATE (m)-[:HAS_CAST]->(a);
