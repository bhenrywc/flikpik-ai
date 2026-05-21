from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import (
    get_movie_recommendations,
    get_personalized_recommendations,
)
from app.services.preference_service import build_user_profile
from app.routes.ratings import ratings_store

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    prompt: str


class PersonalizedChatRequest(BaseModel):
    user_id: str
    prompt: str


@router.post("/recommend")
def recommend_movies(request: ChatRequest):
    response = get_movie_recommendations(request.prompt)

    return {
        "prompt": request.prompt,
        "response": response,
    }


@router.post("/personalized")
def personalized_recommendations(request: PersonalizedChatRequest):
    user_ratings = [
        rating for rating in ratings_store
        if rating["user_id"] == request.user_id
    ]

    user_profile = build_user_profile(user_ratings)

    response = get_personalized_recommendations(
        user_prompt=request.prompt,
        user_profile=user_profile
    )

    return {
        "user_id": request.user_id,
        "profile": user_profile,
        "response": response,
    }