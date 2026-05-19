import re
import requests
from functools import lru_cache
from app.config import TMDB_API_KEY


def clean_title(title: str) -> str:
    return re.sub(r"\s*\(\d{4}\)", "", str(title)).strip()


@lru_cache(maxsize=2048)
def fetch_poster(title: str) -> str | None:
    if not TMDB_API_KEY:
        return None

    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": clean_title(title)}

    try:
        response = requests.get(url, params=params, timeout=8)
        response.raise_for_status()
        results = response.json().get("results", [])
        if not results:
            return None
        poster_path = results[0].get("poster_path")
        return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
    except Exception:
        return None
