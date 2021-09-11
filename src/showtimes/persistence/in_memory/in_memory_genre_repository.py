from typing import List, Union, Dict

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.movie.genre.genre import Genre
from src.showtimes.domain.movie.genre.genre_id import GenreId
from src.showtimes.usecase.movie.genre.genre_extractor import GenreExtractor
from src.showtimes.usecase.movie.genre.genre_persister import GenrePersister


class InMemoryGenreRepository(GenreExtractor, GenrePersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, genre_id: GenreId) -> Union[Genre, None]:
        return self.__storage.get(genre_id)

    def get_by_name(self, name: str) -> Union[Genre, None]:
        for genre in list(self.__storage.values()):
            if genre.name == name:
                return genre

        return None

    def get_all(self) -> List[Genre]:
        return list(self.__storage.values())

    def save(self, genre: Genre) -> None:
        self.__eventPublisher.publish(genre.pop_events())
        self.__storage[genre.id] = genre
