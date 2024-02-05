MATCH (m:Movie), (c:Cast)
WHERE m.id = c.movie_id
CREATE (m)-[:HAS_CAST]->(c);
