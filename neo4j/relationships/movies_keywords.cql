LOAD CSV WITH HEADERS FROM 'file:///keywords.csv' AS row
MATCH (m:Movie {id: toInteger(row.movie_id)})
MATCH (k:Keyword {keyword_id: toInteger(row.id)})
CREATE (m)-[:HAS_KEYWORD]->(k);
