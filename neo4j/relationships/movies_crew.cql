LOAD CSV WITH HEADERS FROM 'file:///crew.csv' AS row
MATCH (m:Movie {id: toInteger(row.movie_id)})
MATCH (c:Crew {crew_id: toInteger(row.id)})
CREATE (m)-[:HAS_CREW]->(c);
