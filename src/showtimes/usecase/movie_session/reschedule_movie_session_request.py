from __future__ import annotations
from dataclasses import dataclass

from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId
from src.showtimes.domain.time_interval.time_interval_id import TimeIntervalId


@dataclass(frozen=True)
class RescheduleMovieSessionRequest:
    time_interval_id: TimeIntervalId
    movie_session_id: MovieSessionId

    @staticmethod
    def from_(
            time_interval_id: str,
            movie_session_id: str,
    ) -> RescheduleMovieSessionRequest:
        return RescheduleMovieSessionRequest(
            TimeIntervalId(time_interval_id),
            MovieSessionId(movie_session_id)
        )
