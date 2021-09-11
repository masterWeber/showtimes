from __future__ import annotations
from dataclasses import dataclass
from typing import Union

from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.domain.time_interval.time_interval_id import TimeIntervalId


@dataclass(frozen=True)
class CreateMovieSessionRequest:
    time_interval_id: TimeIntervalId
    date: date
    movie_id: Union[MovieId, None]

    @staticmethod
    def from_(
            time_interval_id: str,
            date_: date,
            movie_id: Union[str, None] = None,
    ) -> CreateMovieSessionRequest:
        movie_id = None if movie_id is None else MovieId(movie_id)

        return CreateMovieSessionRequest(
            TimeIntervalId(time_interval_id),
            date_,
            movie_id
        )
