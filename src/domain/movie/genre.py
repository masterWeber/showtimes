from __future__ import annotations

from src.domain.movie.genre_id import GenreId
from src.domain.movie.genre_id_generator import GenreIdGenerator


class Genre:
    __id: GenreId
    __name: str

    def __init__(self, id_: GenreId, name: str):
        self.__id = id_
        self.__name = name

    @property
    def id(self) -> GenreId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @staticmethod
    def create(id_generator: GenreIdGenerator, name: str) -> Genre:
        return Genre(id_generator.generate(), name)
