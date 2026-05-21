from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "movies.csv"


def load_movies() -> pd.DataFrame:
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    return pd.DataFrame([
        {"movie_id": 1, "title": "The Dark Knight", "genres": "Action|Crime|Drama"},
        {"movie_id": 2, "title": "Interstellar", "genres": "Adventure|Drama|Sci-Fi"},
        {"movie_id": 3, "title": "Toy Story", "genres": "Animation|Comedy|Family"},
    ])


def get_popular_movies(limit: int = 10):
    movies_df = load_movies()
    return movies_df.head(limit).to_dict(orient="records")


def search_movies(query: str, limit: int = 10):
    movies_df = load_movies()
    results = movies_df[
        movies_df["title"].str.contains(query, case=False, na=False)
    ]
    return results.head(limit).to_dict(orient="records")


def get_similar_movies(title: str, limit: int = 5):
    movies_df = load_movies()

    target_movie = movies_df[
        movies_df["title"].str.contains(title, case=False, na=False)
    ]

    if target_movie.empty:
        return []

    target_title = target_movie.iloc[0]["title"]
    target_genres = str(target_movie.iloc[0]["genres"]).split("|")

    def similarity_score(movie_genres):
        genres = str(movie_genres).split("|")
        return len(set(target_genres) & set(genres))

    temp_df = movies_df.copy()
    temp_df["score"] = temp_df["genres"].apply(similarity_score)

    recommendations = (
        temp_df[temp_df["title"] != target_title]
        .sort_values(by="score", ascending=False)
        .head(limit)
    )

    return recommendations.to_dict(orient="records")
