MATCH (m:Movie), (k:Keyword)
WHERE m.id = k.movie_id
CREATE (m)-[:HAS_KEYWORD]->(k);
