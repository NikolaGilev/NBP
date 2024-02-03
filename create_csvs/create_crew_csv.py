import pandas as pd
import json
from itertools import chain
from json.decoder import JSONDecodeError


def main():
    working_dir = "../datasets/movies_db/"
    df_credits = pd.read_csv(working_dir + "credits.csv")

    data = []
    for index, crew_row in enumerate(df_credits["crew"]):
        data_string = crew_row[1:-1].split("},")
        data_string[-1] = data_string[-1][:-1]
        crew_row_elements = [
            ds + f", 'movie_id': {df_credits.at[index, 'id']}" + "}"
            for ds in data_string
        ]
        data.append(crew_row_elements)

    flattened_data = list(chain(*data))
    cleaned_data = []

    for entry in data:
        try:
            cleaned_data.extend([json.loads(e.replace("'", '"')) for e in entry])
        except JSONDecodeError as e:
            print(f"Skipping entry due to JSONDecodeError: {e}")
            continue

    df = pd.DataFrame(cleaned_data)
    df.to_csv("output_crew.csv", index=False)


main()
