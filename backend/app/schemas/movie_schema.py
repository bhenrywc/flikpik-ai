from pydantic import BaseModel
from typing import Optional

class MovieOut(BaseModel):
    movieId: int
    title: str
    genres: Optional[str] = None
    poster_url: Optional[str] = None
    score: Optional[float] = None
    similarity: Optional[float] = None
    reason: Optional[str] = None

class RatingIn(BaseModel):
    user_id: str = "demo-user"
    movieId: int
    rating: float
