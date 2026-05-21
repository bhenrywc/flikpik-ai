import RatingButtons from "./RatingButtons.jsx";

function MovieCard({ movie, onSimilar }) {
  return (
    <article className="movie-card">
      <div className="poster-frame">
        {movie.poster_url ? (
          <img src={movie.poster_url} alt={`${movie.title} poster`} />
        ) : (
          <div className="poster-placeholder">
            <span>No Poster Yet</span>
          </div>
        )}
      </div>

      <div className="movie-card-body">
        <h3>{movie.title}</h3>
        <p className="genres">{movie.genres}</p>

        {movie.score !== undefined && (
          <p className="score">Similarity score: {movie.score}</p>
        )}

        <div className="card-actions">
          <a href={movie.trailer_url} target="_blank" rel="noreferrer">
            Watch Trailer
          </a>
          <button type="button" onClick={() => onSimilar(movie.title)}>
            More Like This
          </button>
        </div>

        <RatingButtons movie={movie} />
      </div>
    </article>
  );
}

export default MovieCard;
