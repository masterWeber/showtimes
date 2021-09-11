from __future__ import annotations
from dataclasses import dataclass

from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId


@dataclass(frozen=True)
class AddMovieToSessionRequest:
    movie_id: MovieId
    movie_session_id: MovieSessionId

    @staticmethod
    def from_(
            movie_id: str,
            movie_session_id: str,
    ) -> AddMovieToSessionRequest:
        return AddMovieToSessionRequest(
            MovieId(movie_id),
            MovieSessionId(movie_session_id)
        )
