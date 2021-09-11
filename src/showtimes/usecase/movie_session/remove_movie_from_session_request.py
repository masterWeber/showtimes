from __future__ import annotations
from dataclasses import dataclass

from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId


@dataclass(frozen=True)
class RemoveMovieFromSessionRequest:
    movie_session_id: MovieSessionId

    @staticmethod
    def from_(movie_session_id: str) -> RemoveMovieFromSessionRequest:
        return RemoveMovieFromSessionRequest(
            MovieSessionId(movie_session_id)
        )
