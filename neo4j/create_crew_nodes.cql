LOAD CSV WITH HEADERS FROM 'file:///crew.csv' AS row
CREATE (:Crew {
  credit_id: row.credit_id,
  department: row.department,
  gender: toInteger(row.gender),
  crew_id: toInteger(row.id),
  job: row.job,
  name: row.name,
  profile_path: row.profile_path,
  movie_id: toInteger(row.movie_id)
});
