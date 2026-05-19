from fastapi import APIRouter
from app.services.recommender_service import popular_movies, similar_movies

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.get("/popular")
def get_popular(limit: int = 12):
    return {"results": popular_movies(limit)}

@router.get("/similar/{movie_id}")
def get_similar(movie_id: int, limit: int = 12):
    return {"movie_id": movie_id, "results": similar_movies(movie_id, limit)}
