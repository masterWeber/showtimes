from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.movie.country.country import Country
from src.showtimes.domain.movie.country.country_id import CountryId


class CountryExtractor(ABC):

    @abstractmethod
    def get_by_id(self, country_id: CountryId) -> Optional[Country]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Country]:
        pass

    @abstractmethod
    def get_all(self) -> List[Country]:
        pass
