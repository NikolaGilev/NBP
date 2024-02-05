MATCH (m:Movie), (c:Crew)
WHERE m.id = c.movie_id
CREATE (m)-[:HAS_CREW]->(c);