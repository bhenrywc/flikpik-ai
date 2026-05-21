from fastapi import APIRouter, Query

from app.services.vector_service import semantic_movie_search

router = APIRouter(prefix="/discovery", tags=["Discovery"])


@router.get("/semantic-search")
def semantic_search(query: str = Query(...), limit: int = 5):
    return semantic_movie_search(query=query, limit=limit)
