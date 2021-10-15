from typing import List, Dict, Optional

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.movie.country.country import Country
from src.showtimes.domain.movie.country.country_id import CountryId
from src.showtimes.usecase.movie.country.country_extractor import CountryExtractor
from src.showtimes.usecase.movie.country.country_persister import CountryPersister


class InMemoryCountryRepository(CountryExtractor, CountryPersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, country_id: CountryId) -> Optional[Country]:
        return self.__storage.get(country_id)

    def get_by_name(self, name: str) -> Optional[Country]:
        for country in list(self.__storage.values()):
            if country.name == name:
                return country

        return None

    def get_all(self) -> List[Country]:
        return list(self.__storage.values())

    def save(self, country: Country) -> None:
        self.__eventPublisher.publish(country.pop_events())
        self.__storage[country.id] = country
