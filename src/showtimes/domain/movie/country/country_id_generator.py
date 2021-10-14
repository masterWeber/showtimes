from abc import ABC, abstractmethod

from src.showtimes.domain.movie.country.country_id import CountryId


class CountryIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> CountryId:
        pass
