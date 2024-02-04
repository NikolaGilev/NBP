LOAD CSV WITH HEADERS FROM 'file:///keywords.csv' AS row
CREATE (:Keyword {
  keyword_id: toInteger(row.id),
  name: row.name,
  movie_id: toInteger(row.movie_id)
});
