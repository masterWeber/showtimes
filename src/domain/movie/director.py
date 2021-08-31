from __future__ import annotations

from src.domain.common.entity import Entity
from src.domain.movie.director_id import DirectorId
from src.domain.movie.director_id_generator import DirectorIdGenerator


class Director(Entity):
    __id: DirectorId
    __name: str

    def __init__(self, id_: DirectorId, name: str) -> None:
        if not name.strip():
            raise ValueError("The `name` cannot be empty.")

        self.__id = id_
        self.__name = name

    @property
    def id(self) -> DirectorId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @staticmethod
    def create(id_generator: DirectorIdGenerator, name: str) -> Director:
        return Director(id_generator.generate(), name)
