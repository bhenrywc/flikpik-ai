import { useState } from "react";
import { saveRating } from "../services/api.js";

function RatingButtons({ movie }) {
  const [selectedRating, setSelectedRating] = useState(null);

  async function handleRating(rating) {
    setSelectedRating(rating);

    try {
      await saveRating(movie, rating);
    } catch (err) {
      console.error("Failed to save rating:", err);
    }
  }

  return (
    <div className="ratings" id="ratings">
      <span>Your rating:</span>
      <div className="rating-buttons">
        {[1, 2, 3, 4, 5].map((rating) => (
          <button
            key={rating}
            type="button"
            className={selectedRating === rating ? "active-rating" : ""}
            onClick={() => handleRating(rating)}
          >
            {rating}★
          </button>
        ))}
      </div>
    </div>
  );
}

export default RatingButtons;
