LOAD CSV WITH HEADERS FROM 'file:///collections.csv' AS row
CREATE (:Collection {
  collection_id: toInteger(row.id),
  name: row.name,
  poster_path: row.poster_path,
  backdrop_path: row.backdrop_path,
  movie_id: toInteger(row.movie_id)
});
