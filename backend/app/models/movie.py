from pydantic import BaseModel


class Movie(BaseModel):
    movie_id: int
    title: str
    genres: str
    poster_url: str | None = None
    trailer_url: str | None = None
