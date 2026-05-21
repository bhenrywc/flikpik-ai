import MovieCard from "./MovieCard.jsx";

function MovieGrid({ movies, onSimilar }) {
  if (!movies.length) {
    return (
      <div className="empty-state">
        No movies found. Try searching for Batman, Interstellar, Toy Story, or Matrix.
      </div>
    );
  }

  return (
    <div className="movie-grid">
      {movies.map((movie) => (
        <MovieCard key={`${movie.movie_id}-${movie.title}`} movie={movie} onSimilar={onSimilar} />
      ))}
    </div>
  );
}

export default MovieGrid;
