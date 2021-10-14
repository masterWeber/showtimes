from abc import ABC, abstractmethod
from typing import Union, List

from src.showtimes.domain.movie.country.country import Country
from src.showtimes.domain.movie.country.country_id import CountryId


class CountryExtractor(ABC):

    @abstractmethod
    def get_by_id(self, country_id: CountryId) -> Union[Country, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Union[Country, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Country]:
        pass
