LOAD CSV WITH HEADERS FROM 'file:///movies.csv' AS row
CREATE (:Movie {
  for_adults: toBoolean(row.for_adults),
  budget: toInteger(row.budget),
  id: toInteger(row.id),
  imdb_id: row.imdb_id,
  original_language: row.original_language,
  original_title: row.original_title,
  overview: row.overview,
  popularity: toFloat(row.popularity),
  release_date: date(row.release_date, 'yyyy-MM-dd'),
  revenue: toFloat(row.revenue),
  runtime: toInteger(row.runtime),
  title: row.title
});
