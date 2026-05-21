import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_movie_recommendations(user_prompt: str):

    system_prompt = """
    You are FlikPik AI, an intelligent movie discovery assistant.

    Recommend movies based on:
    - mood
    - genre
    - themes
    - actors
    - directors
    - pacing
    - emotional tone

    Keep recommendations concise and engaging.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.8,
        max_tokens=300,
    )

    return response.choices[0].message.content


def get_personalized_recommendations(user_prompt: str, user_profile: dict):

    profile_text = f"""
    User profile:
    Favorite genres: {user_profile.get("favorite_genres")}
    Liked movies: {[m.get("title") for m in user_profile.get("liked_movies", [])]}
    Disliked movies: {[m.get("title") for m in user_profile.get("disliked_movies", [])]}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are FlikPik AI. Recommend movies using the user's taste profile."
            },
            {
                "role": "user",
                "content": profile_text + "\n\nRequest: " + user_prompt
            }
        ],
        temperature=0.7,
        max_tokens=400,
    )

    return response.choices[0].message.content
