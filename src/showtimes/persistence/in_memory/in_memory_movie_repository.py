from typing import List, Dict, Optional

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.movie.movie import Movie
from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.usecase.movie.movie_extractor import MovieExtractor
from src.showtimes.usecase.movie.movie_persister import MoviePersister


class InMemoryMovieRepository(MovieExtractor, MoviePersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, movie_id: MovieId) -> Optional[Movie]:
        return self.__storage.get(movie_id)

    def get_by_name(self, name: str) -> List[Movie]:
        matches: List[Movie] = []

        for movie in list(self.__storage.values()):
            if movie.name == name:
                matches.append(movie)

        return matches

    def get_by_name_and_duration(self, name: str, duration: int) -> Optional[Movie]:
        for movie in list(self.__storage.values()):
            if movie.name == name and movie.duration == duration:
                return movie

        return None

    def get_all(self) -> List[Movie]:
        return list(self.__storage.values())

    def save(self, movie: Movie) -> None:
        self.__eventPublisher.publish(movie.pop_events())
        self.__storage[movie.id] = movie
