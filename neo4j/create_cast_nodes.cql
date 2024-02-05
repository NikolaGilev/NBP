LOAD CSV WITH HEADERS FROM 'file:///cast.csv' AS row
CREATE (:Cast {
  cast_id: toInteger(row.cast_id),
  character: row.character,
  credit_id: row.credit_id,
  gender: toInteger(row.gender),
  actor_id: toInteger(row.id),
  name: row.name,
  order: toInteger(row.order),
  profile_path: row.profile_path,
  movie_id: toInteger(row.movie_id)
});
