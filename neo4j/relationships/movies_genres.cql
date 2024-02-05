MATCH (m:Movie), (g:Genre)
WHERE m.id = g.movie_id
CREATE (m)-[:BELONGS_TO]->(g);