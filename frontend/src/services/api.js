import axios from "axios";

const API_BASE_URL = "https://fictional-lamp-g66469v677rfw9rw-8000.app.github.dev";

export async function getPopularMovies() {
  const response = await axios.get(`${API_BASE_URL}/recommendations/popular`);
  return response.data;
}

export async function searchMovies(query) {
  const response = await axios.get(`${API_BASE_URL}/movies/search`, {
    params: { query },
  });
  return response.data;
}

export async function getSimilarMovies(title) {
  const response = await axios.get(`${API_BASE_URL}/recommendations/similar/${title}`);
  return response.data;
}

export async function saveRating(movie, rating) {
  const response = await axios.post(`${API_BASE_URL}/ratings/`, {
    user_id: "demo-user",
    movie_id: movie.movie_id,
    title: movie.title,
    rating,
  });

  return response.data;
}
