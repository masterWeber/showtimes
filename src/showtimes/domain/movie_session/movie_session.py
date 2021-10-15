from __future__ import annotations
from datetime import date
from typing import Optional

from src.common.entity import Entity
from src.showtimes.domain.time_interval.time_interval import TimeInterval
from src.showtimes.domain.movie.movie import Movie
from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId
from src.showtimes.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator


class MovieSession(Entity):
    __id: MovieSessionId
    __date: date
    __movie: Optional[Movie]
    __interval: TimeInterval

    def __init__(
            self,
            id_: MovieSessionId,
            interval: TimeInterval,
            date_: date,
            movie: Movie = None
    ) -> None:
        self.__id = id_
        self.__date = date_
        self.__movie = movie
        self.__interval = interval

    @property
    def id(self) -> MovieSessionId:
        return self.__id

    @property
    def movie(self) -> Optional[Movie]:
        return self.__movie

    @movie.setter
    def movie(self, movie: Movie) -> None:
        self.__movie = movie

    @property
    def interval(self) -> TimeInterval:
        return self.__interval

    @interval.setter
    def interval(self, interval: TimeInterval) -> None:
        self.__interval = interval

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date_: date) -> None:
        self.__date = date_

    @staticmethod
    def create(
            id_generator: MovieSessionIdGenerator,
            interval: TimeInterval,
            date_: date,
            movie: Optional[Movie] = None
    ) -> MovieSession:
        return MovieSession(id_generator.generate(), interval, date_, movie)

    def movie_is_fit_in_interval(self) -> bool:
        return self.free_time() >= 0

    def free_time(self) -> int:
        if self.is_empty():
            raise ValueError("`Movie` not specified.")

        return self.interval.duration - self.movie.duration

    def is_empty(self) -> bool:
        return self.movie is None

    def remove_movie(self) -> None:
        self.movie = None

    def reschedule(self, interval: TimeInterval) -> None:
        self.interval = interval
