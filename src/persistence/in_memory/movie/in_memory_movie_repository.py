from typing import List, Union, Dict

from src.domain.common.event.domain_event_publisher import DomainEventPublisher
from src.domain.movie.movie import Movie
from src.domain.movie.movie_id import MovieId
from src.usecase.movie.movie_extractor import MovieExtractor
from src.usecase.movie.movie_persister import MoviePersister


class InMemoryMovieRepository(MovieExtractor, MoviePersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, movie_id: MovieId) -> Union[Movie, None]:
        return self.__storage.get(movie_id)

    def get_all(self) -> List[Movie]:
        return list(self.__storage.values())

    def save(self, movie: Movie) -> None:
        self.__eventPublisher.publish(movie.pop_events())
        self.__storage[movie.id] = movie
