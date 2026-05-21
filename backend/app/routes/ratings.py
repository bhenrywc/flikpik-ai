from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/ratings", tags=["Ratings"])

ratings_store = []


class Rating(BaseModel):
    user_id: str = "demo-user"
    movie_id: int
    title: str
    rating: int = Field(..., ge=1, le=5)


@router.post("/")
def save_rating(rating: Rating):
    ratings_store.append(rating.model_dump())
    return {
        "message": "Rating saved",
        "rating": rating
    }


@router.get("/{user_id}")
def get_user_ratings(user_id: str):
    return [rating for rating in ratings_store if rating["user_id"] == user_id]
