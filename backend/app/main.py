from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI(title="FlikPik AI API")

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
    return movies_df.head(10).to_dict(orient="records")

@app.get("/movies/search")
def search_movies(query: str = Query(...)):
    results = movies_df[
        movies_df["title"].str.contains(query, case=False, na=False)
    ]

    return results.to_dict(orient="records")

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

    movies_df["score"] = movies_df["genres"].apply(similarity_score)

    recommendations = (
        movies_df[movies_df["title"] != target_movie.iloc[0]["title"]]
        .sort_values(by="score", ascending=False)
        .head(5)
    )

    return recommendations.to_dict(orient="records")