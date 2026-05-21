import os
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

from app.services.recommender_service import get_popular_movies
from app.services.media_service import enrich_movie

ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDING_MODEL = "text-embedding-3-small"

_cached_movie_vectors = None


def get_embedding(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return np.array(response.data[0].embedding)


def movie_to_text(movie: dict):
    return f"{movie.get('title', '')}. Genres: {movie.get('genres', '')}"


def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def build_movie_vectors():
    global _cached_movie_vectors

    if _cached_movie_vectors is not None:
        return _cached_movie_vectors

    movies = get_popular_movies(limit=50)

    vectors = []
    for movie in movies:
        text = movie_to_text(movie)
        embedding = get_embedding(text)

        vectors.append({
            "movie": movie,
            "embedding": embedding,
        })

    _cached_movie_vectors = vectors
    return vectors


def semantic_movie_search(query: str, limit: int = 5):
    query_embedding = get_embedding(query)
    movie_vectors = build_movie_vectors()

    scored = []

    for item in movie_vectors:
        score = cosine_similarity(query_embedding, item["embedding"])

        movie = item["movie"].copy()
        movie["semantic_score"] = round(score, 4)

        scored.append(movie)

    ranked = sorted(
        scored,
        key=lambda x: x["semantic_score"],
        reverse=True
    )

    return [enrich_movie(movie) for movie in ranked[:limit]]
