from abc import ABC, abstractmethod

from src.showtimes.domain.movie.country.country import Country


class CountryPersister(ABC):

    @abstractmethod
    def save(self, country: Country) -> None:
        pass
