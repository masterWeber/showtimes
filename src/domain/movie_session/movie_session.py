from __future__ import annotations
from datetime import date
from typing import Union

from src.domain.common.entity import Entity
from src.domain.movie_session.interval import Interval
from src.domain.movie.movie import Movie
from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator


class MovieSession(Entity):
    __id: MovieSessionId
    __date: date
    __movie: Union[Movie, None]
    __interval: Interval

    def __init__(self, id_: MovieSessionId, interval: Interval, date_: date, movie: Movie = None) -> None:
        self.__id = id_
        self.__date = date_
        self.__movie = movie
        self.__interval = interval

    @property
    def id(self) -> MovieSessionId:
        return self.__id

    @property
    def movie(self) -> Union[Movie, None]:
        return self.__movie

    @movie.setter
    def movie(self, movie: Movie) -> None:
        self.__movie = movie

    @property
    def interval(self) -> Interval:
        return self.__interval

    @interval.setter
    def interval(self, interval: Interval) -> None:
        self.__interval = interval

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date_: date) -> None:
        self.__date = date_

    @staticmethod
    def create(id_generator: MovieSessionIdGenerator, interval: Interval, date_: date) -> MovieSession:
        return MovieSession(id_generator.generate(), interval, date_)

    def movie_is_fit_in_interval(self) -> bool:
        return self.get_free_time() >= 0

    def get_free_time(self) -> int:
        if self.is_empty():
            raise ValueError("`Movie` not specified.")

        return self.interval.duration - self.movie.duration

    def is_empty(self) -> bool:
        return self.movie is None
