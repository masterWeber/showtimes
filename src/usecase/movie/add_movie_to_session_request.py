from __future__ import annotations
from dataclasses import dataclass

from src.domain.movie.movie_id import MovieId
from src.domain.movie_session.movie_session_id import MovieSessionId


@dataclass(frozen=True)
class AddMovieToSessionRequest:
    movie_id: MovieId
    movie_session_id: MovieSessionId

    @staticmethod
    def from_(
            movie_id: int,
            movie_session_id: int,
    ) -> AddMovieToSessionRequest:
        return AddMovieToSessionRequest(
            MovieId(movie_id),
            MovieSessionId(movie_session_id)
        )
