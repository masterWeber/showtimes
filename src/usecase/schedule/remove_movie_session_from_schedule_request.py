from __future__ import annotations
from dataclasses import dataclass

from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.schedule.schedule_id import MovieSessionId


@dataclass(frozen=True)
class RemoveMovieSessionFromScheduleRequest:
    movie_session_id: MovieSessionId
    schedule_id: MovieSessionId

    @staticmethod
    def from_(
            movie_session_id: int,
            schedule_id: int,
    ) -> RemoveMovieSessionFromScheduleRequest:
        return RemoveMovieSessionFromScheduleRequest(
            MovieSessionId(movie_session_id),
            MovieSessionId(schedule_id),
        )
