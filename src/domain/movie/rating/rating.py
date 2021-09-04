from __future__ import annotations

from src.domain.common.entity import Entity
from src.domain.movie.rating.rating_id import RatingId
from src.domain.movie.rating.rating_id_generator import RatingIdGenerator
from src.domain.movie.rating.rating_type import RatingType


class Rating(Entity):
    __id: RatingId
    __type: RatingType
    __score: float

    def __init__(self, id_: RatingId, type_: RatingType, score: float) -> None:
        self.__id = id_
        self.__type = type_
        self.__score = score

    @property
    def id(self) -> RatingId:
        return self.__id

    @property
    def type(self) -> RatingType:
        return self.__type

    @type.setter
    def type(self, type_: RatingType) -> None:
        self.__type = type_

    @property
    def score(self) -> float:
        return self.__score

    @score.setter
    def score(self, score: float) -> None:
        self.__score = score

    @staticmethod
    def create(
            id_generator: RatingIdGenerator,
            type_: RatingType,
            score: float
    ) -> Rating:
        return Rating(id_generator.generate(), type_, score)
