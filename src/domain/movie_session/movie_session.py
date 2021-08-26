from __future__ import annotations
from datetime import date

from src.domain.movie_session.interval import Interval
from src.domain.movie.movie import Movie
from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator


class MovieSession:
    __id: MovieSessionId
    __date: date
    __movie: Movie
    __interval: Interval

    def __init__(self, id_: MovieSessionId, date_: date, movie: Movie = None, interval: Interval = None):
        self.__id = id_
        self.__date = date_
        self.__movie = movie
        self.__interval = interval

    @property
    def id(self) -> MovieSessionId:
        return self.__id

    @property
    def movie(self) -> Movie:
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
    def create(id_generator: MovieSessionIdGenerator) -> MovieSession:
        return MovieSession(id_generator.generate(), date.today())

    def movie_is_fit_in_interval(self) -> bool:
        return self.get_free_time() >= 0

    def get_free_time(self) -> int:
        return self.interval.duration - self.movie.duration
