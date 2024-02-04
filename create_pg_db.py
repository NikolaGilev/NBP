import psycopg2
from sqlalchemy import create_engine
import pandas as pd

db_params = {
    "user": "postgres",
    "password": "postgres",
    "dbname": "nbp",
    "host": "localhost",
    "port": 5433,
}

conn = psycopg2.connect(**db_params)

cast_csv_path = "./csvs/cast.csv"
collection_csv_path = "./csvs/collections.csv"
crew_csv_path = "./csvs/crew.csv"
genres_csv_path = "./csvs/genres.csv"
keywords_csv_path = "./csvs/keywords.csv"
movies_csv_path = "./csvs/movies.csv"

cast_df = pd.read_csv(cast_csv_path)
collection_df = pd.read_csv(collection_csv_path)
crew_df = pd.read_csv(crew_csv_path)
genres_df = pd.read_csv(genres_csv_path)
keywords_df = pd.read_csv(keywords_csv_path)
movies_df = pd.read_csv(movies_csv_path)

cast_table_name = "cast"
collection_table_name = "collections"
crew_table_name = "crew"
genres_table_name = "genres"
keywords_table_name = "keywords"
movies_table_name = "movies"


engine = create_engine(
    f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}'
)

cast_df.drop(["order"], axis=1, inplace=True)
collection_df.drop(columns=[" "], axis=1, inplace=True)
genres_df.drop(columns=[" "], axis=1, inplace=True)
movies_df.drop_duplicates(subset="id", keep="first", inplace=True)

cast_df.to_sql(cast_table_name, engine, if_exists="append", index=False)
collection_df.to_sql(collection_table_name, engine, if_exists="append", index=False)
crew_df.to_sql(crew_table_name, engine, if_exists="append", index=False)
genres_df.to_sql(genres_table_name, engine, if_exists="append", index=False)
keywords_df.to_sql(keywords_table_name, engine, if_exists="append", index=False)
movies_df.to_sql(movies_table_name, engine, if_exists="append", index=False)


conn.close()
