LOAD CSV WITH HEADERS FROM 'file:///collections.csv' AS row
MATCH (m:Movie {id: toInteger(row.movie_id)})
MATCH (c:Collection {collection_id: toInteger(row.id)})
CREATE (m)-[:PART_OF_COLLECTION]->(c);
