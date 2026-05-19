from fastapi import FastAPI

app = FastAPI(title="FlikPik AI API")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "FlikPik API is running"
    }