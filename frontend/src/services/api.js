const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export async function getPopularMovies() {
  const res = await fetch(`${API_BASE}/recommendations/popular?limit=12`);
  return res.json();
}

export async function searchMovies(query) {
  const res = await fetch(`${API_BASE}/movies/search?query=${encodeURIComponent(query)}&limit=12`);
  return res.json();
}

export async function getSimilarMovies(movieId) {
  const res = await fetch(`${API_BASE}/recommendations/similar/${movieId}?limit=12`);
  return res.json();
}
