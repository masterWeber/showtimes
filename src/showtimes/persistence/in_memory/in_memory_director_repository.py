from typing import List, Union, Dict

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.movie.director.director import Director
from src.showtimes.domain.movie.director.director_id import DirectorId
from src.showtimes.usecase.movie.director.director_extractor import DirectorExtractor
from src.showtimes.usecase.movie.director.director_persister import DirectorPersister


class InMemoryDirectorRepository(DirectorExtractor, DirectorPersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, director_id: DirectorId) -> Union[Director, None]:
        return self.__storage.get(director_id)

    def get_by_name(self, name: str) -> Union[Director, None]:
        for director in list(self.__storage.values()):
            if director.name == name:
                return director

        return None

    def get_all(self) -> List[Director]:
        return list(self.__storage.values())

    def save(self, director: Director) -> None:
        self.__eventPublisher.publish(director.pop_events())
        self.__storage[director.id] = director
