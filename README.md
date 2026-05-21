# FlikPik AI - Phase 1 MVP

AI-powered movie discovery MVP built with FastAPI + React.

## Features

- Modern React UI
- FastAPI backend
- Movie search
- Movie cards with posters
- Popular recommendations
- Similar movie recommendations
- Basic user ratings
- TMDB poster support
- YouTube trailer links

## Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Test:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/recommendations/popular
http://127.0.0.1:8000/movies/search?query=batman
http://127.0.0.1:8000/recommendations/similar/Interstellar
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

## Environment Variables

Create `backend/.env`:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

Without a TMDB key, the app still works, but poster URLs will be null.
