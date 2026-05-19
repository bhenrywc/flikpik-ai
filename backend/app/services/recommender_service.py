import sys
from functools import lru_cache
from pathlib import Path
import pandas as pd

from app.config import DATA_DIR, ML_SRC_DIR
from app.services.tmdb_service import fetch_poster

# Reuse your existing Streamlit recommender class without rewriting it yet.
sys.path.append(str(ML_SRC_DIR))
from recommender import HybridRecommender  # noqa: E402


def _safe_float(value):
    try:
        return round(float(value), 4)
    except Exception:
        return None


def _format_movie(row, score_col=None, include_poster=True, reason=None):
    title = str(row.get("title", ""))
    movie = {
        "movieId": int(row.get("movieId")),
        "title": title,
        "genres": None if pd.isna(row.get("genres")) else str(row.get("genres")),
        "poster_url": fetch_poster(title) if include_poster else None,
        "score": _safe_float(row.get(score_col)) if score_col else None,
        "similarity": _safe_float(row.get("similarity")),
        "reason": reason,
    }
    return movie


@lru_cache(maxsize=1)
def load_data():
    movies = pd.read_csv(DATA_DIR / "movies_clean.csv")
    ratings = pd.read_csv(DATA_DIR / "ratings_clean.csv")
    genres = pd.read_csv(DATA_DIR / "genre_encoded.csv")
    popularity_path = DATA_DIR / "popularity_df.csv"
    popularity = pd.read_csv(popularity_path) if popularity_path.exists() else None
    return movies, ratings, genres, popularity


@lru_cache(maxsize=1)
def get_model():
    movies, ratings, genres, _ = load_data()
    model = HybridRecommender(
        train_df=ratings,
        movies_df=movies,
        genre_df=genres,
        n_components=50,
        neighbor_k=15,
    )
    return model.fit()


def search_movies(query: str, limit: int = 12):
    model = get_model()
    results = model.find_movies_by_title(query).head(limit)
    return [_format_movie(row, include_poster=True) for _, row in results.iterrows()]


def popular_movies(limit: int = 12):
    model = get_model()
    results = model._popularity_fallback(top_n=limit)
    return [
        _format_movie(row, score_col="weighted_score", include_poster=True, reason="Popular with strong average ratings.")
        for _, row in results.iterrows()
    ]


def similar_movies(movie_id: int, limit: int = 12):
    model = get_model()
    results = model.get_similar_movies(movie_id, n_neighbors=limit)
    return [
        _format_movie(row, score_col="similarity", include_poster=True, reason="Similar viewing patterns from the recommender model.")
        for _, row in results.iterrows()
    ]
