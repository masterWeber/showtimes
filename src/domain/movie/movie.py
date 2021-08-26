from __future__ import annotations
from typing import List

from src.domain.movie.director import Director
from src.domain.movie.genre import Genre
from src.domain.movie.movie_id import MovieId
from src.domain.movie.movie_id_generator import MovieIdGenerator


class Movie:
    __id: MovieId
    __name: str
    __description: str
    __genres: List[Genre]
    __director: Director
    __duration: int
    __year: int
    __poster: str
    __trailer: str

    def __init__(self, id_: MovieId, name: str) -> None:
        self.__id = id_
        self.__name = name

    @property
    def id(self) -> MovieId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @property
    def genres(self) -> List[Genre]:
        return self.__genres

    @genres.setter
    def genres(self, genres: List[Genre]) -> None:
        self.__genres = genres

    def add_genre(self, genre: Genre) -> None:
        self.__genres.append(genre)

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director) -> None:
        self.__director = director

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int) -> None:
        self.__duration = duration

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        self.__year = year

    @property
    def poster(self) -> str:
        return self.__poster

    @poster.setter
    def poster(self, poster: str) -> None:
        self.__poster = poster

    @property
    def trailer(self) -> str:
        return self.__trailer

    @trailer.setter
    def trailer(self, trailer: str) -> None:
        self.__trailer = trailer

    @staticmethod
    def create(id_generator: MovieIdGenerator, name: str) -> Movie:
        return Movie(id_generator.generate(), name)
