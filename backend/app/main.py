import os
import requests
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Query

load_dotenv()

app = FastAPI(title="FlikPik AI API")

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

movies_df = pd.DataFrame([
    {"movie_id": 1, "title": "The Dark Knight", "genres": "Action|Crime|Drama"},
    {"movie_id": 2, "title": "Interstellar", "genres": "Adventure|Drama|Sci-Fi"},
    {"movie_id": 3, "title": "Toy Story", "genres": "Animation|Comedy|Family"},
    {"movie_id": 4, "title": "Inception", "genres": "Action|Sci-Fi|Thriller"},
    {"movie_id": 5, "title": "Black Panther", "genres": "Action|Adventure|Sci-Fi"},
    {"movie_id": 6, "title": "The Matrix", "genres": "Action|Sci-Fi"},
    {"movie_id": 7, "title": "Finding Nemo", "genres": "Animation|Adventure|Comedy"},
    {"movie_id": 8, "title": "Avengers Endgame", "genres": "Action|Adventure|Sci-Fi"},
    {"movie_id": 9, "title": "Joker", "genres": "Crime|Drama|Thriller"},
    {"movie_id": 10, "title": "Shrek", "genres": "Animation|Comedy|Fantasy"},
    {"movie_id": 11, "title": "Batman Begins", "genres": "Action|Crime|Drama"},
])


def get_poster_url(title):
    if not TMDB_API_KEY:
        return None

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": title
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    results = response.json().get("results", [])

    if not results:
        return None

    poster_path = results[0].get("poster_path")

    if not poster_path:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"


def get_trailer_url(title):
    search_query = title.replace(" ", "+")
    return f"https://www.youtube.com/results?search_query={search_query}+official+trailer"


def enrich_movie(movie):
    title = movie["title"]

    return {
        **movie,
        "poster_url": get_poster_url(title),
        "trailer_url": get_trailer_url(title)
    }


@app.get("/")
def root():
    return {
        "message": "Welcome to FlikPik AI API",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "FlikPik API is running"
    }


@app.get("/recommendations/popular")
def popular_movies():
    movies = movies_df.head(10).to_dict(orient="records")
    return [enrich_movie(movie) for movie in movies]


@app.get("/movies/search")
def search_movies(query: str = Query(...)):
    results = movies_df[
        movies_df["title"].str.contains(query, case=False, na=False)
    ]

    movies = results.to_dict(orient="records")
    return [enrich_movie(movie) for movie in movies]


@app.get("/recommendations/similar/{title}")
def similar_movies(title: str):
    target_movie = movies_df[
        movies_df["title"].str.contains(title, case=False, na=False)
    ]

    if target_movie.empty:
        return {"message": "Movie not found"}

    target_genres = target_movie.iloc[0]["genres"].split("|")

    def similarity_score(movie_genres):
        genres = movie_genres.split("|")
        return len(set(target_genres) & set(genres))

    temp_df = movies_df.copy()
    temp_df["score"] = temp_df["genres"].apply(similarity_score)

    recommendations = (
        temp_df[temp_df["title"] != target_movie.iloc[0]["title"]]
        .sort_values(by="score", ascending=False)
        .head(5)
    )

    movies = recommendations.to_dict(orient="records")
    return [enrich_movie(movie) for movie in movies]