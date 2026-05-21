import os

import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


def get_poster_url(title: str):
    if not TMDB_API_KEY:
        return None

    params = {
        "api_key": TMDB_API_KEY,
        "query": title
    }

    try:
        response = requests.get(TMDB_SEARCH_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return None

    results = response.json().get("results", [])

    if not results:
        return None

    poster_path = results[0].get("poster_path")

    if not poster_path:
        return None

    return f"{TMDB_IMAGE_BASE_URL}{poster_path}"


def get_trailer_url(title: str):
    query = title.replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={query}+official+trailer"


def enrich_movie(movie: dict):
    title = movie.get("title", "")

    return {
        **movie,
        "poster_url": get_poster_url(title),
        "trailer_url": get_trailer_url(title)
    }
