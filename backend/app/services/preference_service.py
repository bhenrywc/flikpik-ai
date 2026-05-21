from collections import Counter


def build_user_profile(ratings: list[dict]):

    liked_movies = [
        rating for rating in ratings
        if rating.get("rating", 0) >= 4
    ]

    disliked_movies = [
        rating for rating in ratings
        if rating.get("rating", 0) <= 2
    ]

    genre_counter = Counter()

    for movie in liked_movies:
        genres = movie.get("genres", "")

        for genre in genres.split("|"):
            if genre:
                genre_counter[genre] += 1

    return {
        "liked_movies": liked_movies,
        "disliked_movies": disliked_movies,
        "favorite_genres": genre_counter.most_common(5),
        "summary": f"User likes {', '.join([g[0] for g in genre_counter.most_common(3)])}"
    }
