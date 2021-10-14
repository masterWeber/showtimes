from __future__ import annotations

from src.common.entity import Entity
from src.showtimes.domain.movie.country.country_id import CountryId
from src.showtimes.domain.movie.country.country_id_generator import CountryIdGenerator


class Country(Entity):
    __id: CountryId
    __name: str

    def __init__(self, id_: CountryId, name: str) -> None:
        if not name.strip():
            raise ValueError("The `name` cannot be empty.")

        self.__id = id_
        self.__name = name.strip()

    @property
    def id(self) -> CountryId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @staticmethod
    def create(id_generator: CountryIdGenerator, name: str) -> Country:
        return Country(id_generator.generate(), name)
