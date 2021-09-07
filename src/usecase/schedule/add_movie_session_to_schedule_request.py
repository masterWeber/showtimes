from __future__ import annotations
from dataclasses import dataclass

from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.schedule.schedule_id import ScheduleId


@dataclass(frozen=True)
class AddMovieSessionToScheduleRequest:
    movie_session_id: MovieSessionId
    schedule_id: ScheduleId
    date: date

    @staticmethod
    def from_(
            movie_session_id: int,
            schedule_id: int,
            date_: date,
    ) -> AddMovieSessionToScheduleRequest:
        return AddMovieSessionToScheduleRequest(
            MovieSessionId(movie_session_id),
            ScheduleId(schedule_id),
            date_
        )
