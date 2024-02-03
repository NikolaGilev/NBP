import pandas as pd
import json
from itertools import chain
from json.decoder import JSONDecodeError


def main():
    working_dir = "../datasets/movies_db/"
    df_keywords = pd.read_csv(working_dir + "keywords.csv")

    data = []
    for index, keyword_row in enumerate(df_keywords["keywords"]):
        data_string = keyword_row[1:-1].split("},")
        data_string[-1] = data_string[-1][:-1]
        keyword_row_elements = [
            ds + f", 'movie_id': {df_keywords.at[index, 'id']}" + "}"
            for ds in data_string
        ]
        data.append(keyword_row_elements)

    flattened_data = list(chain(*data))
    cleaned_data = []

    for entry in data:
        try:
            cleaned_data.extend([json.loads(e.replace("'", '"')) for e in entry])
        except JSONDecodeError as e:
            print(f"Skipping entry due to JSONDecodeError: {e}")
            continue

    df = pd.DataFrame(cleaned_data)
    df.to_csv("output_keyword.csv", index=False)


main()
