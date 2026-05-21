from fastapi import APIRouter

from app.services.recommender_service import get_popular_movies, get_similar_movies
from app.services.media_service import enrich_movie

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.get("/popular")
def popular_movies(limit: int = 10):
    movies = get_popular_movies(limit=limit)
    return [enrich_movie(movie) for movie in movies]


@router.get("/similar/{title}")
def similar_movies(title: str, limit: int = 5):
    movies = get_similar_movies(title=title, limit=limit)
    if not movies:
        return {"message": "Movie not found"}
    return [enrich_movie(movie) for movie in movies]
