

import os
import re
import requests

TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")

def clean_title(title):
    return re.sub(r"\s*\(\d{4}\)", "", str(title)).strip()

def fetch_poster(movie_title):
    if not TMDB_API_KEY:
        return None

    title = clean_title(movie_title)

    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": title
    }

    try:
        response = requests.get(url, params=params, timeout=8)
        data = response.json()

        results = data.get("results", [])
        if results:
            poster_path = results[0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except Exception:
        return None

    return None
