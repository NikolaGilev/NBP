import pandas as pd


def main():
    working_dir = "../datasets/"
    df_movies = pd.read_csv(working_dir + "movies_metadata.csv")

    columns_to_remove = [
        "belongs_to_collection",
        "genres",
        "video",
        "homepage",
        "poster_path",
        "status",
        "vote_average",
        "spoken_languages",
        "tagline",
        "vote_count",
        "production_companies",
        "production_countries",
    ]
    df_movies = df_movies.drop(columns=columns_to_remove)
    df_movies = df_movies.rename(columns={"adult": "for_adults"})

    df_movies.to_csv("output_movies.csv", index=False)


main()
