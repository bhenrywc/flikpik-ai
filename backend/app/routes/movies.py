from fastapi import APIRouter, Query
from app.services.recommender_service import search_movies

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/search")
def movie_search(query: str = Query(..., min_length=1), limit: int = 12):
    return {"query": query, "results": search_movies(query, limit)}
