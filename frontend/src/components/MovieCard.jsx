import React from "react";

export default function MovieCard({ movie, onSimilar }) {
  const saveRating = (rating) => {
    const current = JSON.parse(localStorage.getItem("flikpik_ratings") || "[]");
    const updated = [...current.filter((r) => r.movieId !== movie.movieId), { movieId: movie.movieId, title: movie.title, rating }];
    localStorage.setItem("flikpik_ratings", JSON.stringify(updated));
    alert(`Saved ${rating} stars for ${movie.title}`);
  };

  return (
    <div className="movie-card">
      <div className="poster-wrap">
        {movie.poster_url ? <img src={movie.poster_url} alt={movie.title} /> : <div className="poster-fallback">No Poster</div>}
      </div>
      <h3>{movie.title}</h3>
      <p className="genres">{movie.genres}</p>
      {movie.reason && <p className="reason">{movie.reason}</p>}
      <div className="buttons">
        {[1, 2, 3, 4, 5].map((n) => <button key={n} onClick={() => saveRating(n)}>{n}★</button>)}
      </div>
      <button className="similar" onClick={() => onSimilar(movie.movieId)}>Find Similar</button>
    </div>
  );
}
