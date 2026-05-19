import React, { useEffect, useState } from "react";
import { getPopularMovies, searchMovies, getSimilarMovies } from "./services/api";
import MovieCard from "./components/MovieCard";
import "./styles.css";

export default function App() {
  const [movies, setMovies] = useState([]);
  const [query, setQuery] = useState("");
  const [title, setTitle] = useState("Popular Picks");
  const [loading, setLoading] = useState(false);

  async function loadPopular() {
    setLoading(true);
    const data = await getPopularMovies();
    setMovies(data.results || []);
    setTitle("Popular Picks");
    setLoading(false);
  }

  async function handleSearch(e) {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    const data = await searchMovies(query);
    setMovies(data.results || []);
    setTitle(`Search Results: ${query}`);
    setLoading(false);
  }

  async function handleSimilar(movieId) {
    setLoading(true);
    const data = await getSimilarMovies(movieId);
    setMovies(data.results || []);
    setTitle("Similar Movies");
    setLoading(false);
  }

  useEffect(() => { loadPopular(); }, []);

  return (
    <main>
      <section className="hero">
        <h1>FlikPik</h1>
        <p>Netflix meets ChatGPT — starting with a full-stack movie discovery MVP.</p>
        <form onSubmit={handleSearch}>
          <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search Toy Story, Batman, Matrix..." />
          <button>Search</button>
          <button type="button" onClick={loadPopular}>Popular</button>
        </form>
      </section>

      <h2>{title}</h2>
      {loading ? <p>Loading movies...</p> : <section className="grid">{movies.map((movie) => <MovieCard key={movie.movieId} movie={movie} onSimilar={handleSimilar} />)}</section>}
    </main>
  );
}
