from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import get_movie_recommendations

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    prompt: str


@router.post("/recommend")
def recommend_movies(request: ChatRequest):

    response = get_movie_recommendations(request.prompt)

    return {
        "prompt": request.prompt,
        "response": response,
    }
