from fastapi import APIRouter, Query

from app.services.recommender_service import search_movies
from app.services.media_service import enrich_movie

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/search")
def movie_search(query: str = Query(..., min_length=1), limit: int = 10):
    movies = search_movies(query=query, limit=limit)
    return [enrich_movie(movie) for movie in movies]
