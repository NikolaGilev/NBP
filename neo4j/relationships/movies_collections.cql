MATCH (m:Movie), (c:Collection)
WHERE m.id = c.movie_id
CREATE (m)-[:PART_OF_COLLECTION]->(c);