LOAD CSV WITH HEADERS FROM 'file:///genres.csv' AS row
CREATE (:Genre {
  genre_id: toInteger(row.id),
  name: row.name,
  movie_id: toInteger(row.movie_id)
});
