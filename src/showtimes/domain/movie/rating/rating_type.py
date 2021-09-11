from __future__ import annotations

from src.common.entity import Entity
from src.showtimes.domain.movie.rating.rating_type_id import RatingTypeId
from src.showtimes.domain.movie.rating.rating_type_id_generator import RatingTypeIdGenerator


class RatingType(Entity):
    __id: RatingTypeId
    __name: str

    def __init__(self, id_: RatingTypeId, name: str) -> None:
        if not name.strip():
            raise ValueError("The `name` cannot be empty.")

        self.__id = id_
        self.__name = name

    @property
    def id(self) -> RatingTypeId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @staticmethod
    def create(id_generator: RatingTypeIdGenerator, name: str) -> RatingType:
        return RatingType(id_generator.generate(), name)
