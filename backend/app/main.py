from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import router as health_router
from app.routes.movies import router as movies_router
from app.routes.recommendations import router as recommendations_router
from app.routes.ratings import router as ratings_router

app = FastAPI(title="FlikPik AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fictional-lamp-g66469v677rfw9rw-5173.app.github.dev",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(movies_router)
app.include_router(recommendations_router)
app.include_router(ratings_router)


@app.get("/")
def root():
    return {
        "message": "Welcome cto FlikPik AI API",
        "docs": "/docs",
        "health": "/health"
    }
