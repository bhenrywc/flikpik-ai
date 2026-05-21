import { useEffect, useState } from "react";
import MovieGrid from "./components/MovieGrid.jsx";
import Navbar from "./components/Navbar.jsx";
import SearchBar from "./components/SearchBar.jsx";
import LoadingSpinner from "./components/LoadingSpinner.jsx";
import { getPopularMovies, getSimilarMovies, searchMovies } from "./services/api.js";

function App() {
  const [movies, setMovies] = useState([]);
  const [headline, setHeadline] = useState("Popular Picks");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function loadPopularMovies() {
    setLoading(true);
    setError("");

    try {
      const data = await getPopularMovies();
      setMovies(data);
      setHeadline("Popular Picks");
    } catch (err) {
      setError("Could not load popular movies. Make sure the FastAPI backend is running.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadPopularMovies();
  }, []);

  async function handleSearch(query) {
    setLoading(true);
    setError("");

    try {
      const data = await searchMovies(query);
      setMovies(Array.isArray(data) ? data : []);
      setHeadline(`Search results for "${query}"`);
    } catch (err) {
      setError("Search failed. Check the backend server.");
    } finally {
      setLoading(false);
    }
  }

  async function handleSimilar(title) {
    setLoading(true);
    setError("");

    try {
      const data = await getSimilarMovies(title);
      setMovies(Array.isArray(data) ? data : []);
      setHeadline(`Movies like ${title}`);
    } catch (err) {
      setError("Could not load similar movies.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <Navbar />

      <main className="hero">
        <section className="hero-copy">
          <p className="eyebrow">Phase 1 MVP</p>
          <h1>FlikPik AI</h1>
          <p>
            Discover movies through search, recommendations, posters, trailers,
            and taste-based rating signals.
          </p>
        </section>

        <SearchBar onSearch={handleSearch} onReset={loadPopularMovies} />
      </main>

      <section className="content-section">
        <div className="section-header">
          <h2>{headline}</h2>
          <button className="secondary-button" onClick={loadPopularMovies}>
            Reset
          </button>
        </div>

        {error && <div className="error-box">{error}</div>}
        {loading ? (
          <LoadingSpinner />
        ) : (
          <MovieGrid movies={movies} onSimilar={handleSimilar} />
        )}
      </section>
    </div>
  );
}

export default App;
