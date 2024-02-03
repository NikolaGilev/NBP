import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Database connection parameters
db_params = {
    "user": "postgres",
    "password": "postgres",
    "dbname": "nbp",
    "host": "localhost",
    "port": 5433,
}

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# File paths
cast_csv_path = "cast.csv"
crew_csv_path = "crew.csv"

# Read CSV files into DataFrames
cast_df = pd.read_csv(cast_csv_path)
crew_df = pd.read_csv(crew_csv_path)

# Define table names
cast_table_name = "cast"
crew_table_name = "crew"

# Create a SQLAlchemy engine
engine = create_engine(
    f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}'
)

# Write DataFrames to PostgreSQL tables
cast_df.to_sql(cast_table_name, engine, if_exists="replace", index=False)
crew_df.to_sql(crew_table_name, engine, if_exists="replace", index=False)

# Close the connection
conn.close()
