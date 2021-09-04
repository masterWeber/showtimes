from __future__ import annotations
from dataclasses import dataclass

from src.domain.time_interval.time_interval_id import TimeIntervalId


@dataclass(frozen=True)
class AddMovieSessionToScheduleRequest:
    time_interval_id: TimeIntervalId
    date: date

    @staticmethod
    def from_(
            time_interval_id: int,
            date_: date,
    ) -> AddMovieSessionToScheduleRequest:
        return AddMovieSessionToScheduleRequest(
            TimeIntervalId(time_interval_id),
            date_
        )
