from fastapi import APIRouter
from app.schemas.movie_schema import RatingIn

router = APIRouter(prefix="/ratings", tags=["ratings"])

# Phase 1: frontend saves locally; this endpoint proves the API contract.
# Phase 2: replace this with Supabase/PostgreSQL insert logic.
@router.post("")
def save_rating(rating: RatingIn):
    return {"status": "saved_for_demo", "rating": rating.model_dump()}
