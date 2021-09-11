from __future__ import annotations
from dataclasses import dataclass

from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId
from src.showtimes.domain.schedule.schedule_id import ScheduleId


@dataclass(frozen=True)
class RemoveMovieSessionFromScheduleRequest:
    movie_session_id: MovieSessionId
    schedule_id: ScheduleId

    @staticmethod
    def from_(
            movie_session_id: str,
            schedule_id: str,
    ) -> RemoveMovieSessionFromScheduleRequest:
        return RemoveMovieSessionFromScheduleRequest(
            MovieSessionId(movie_session_id),
            ScheduleId(schedule_id),
        )
