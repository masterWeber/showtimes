from typing import List, Union, Dict

from src.domain.common.event.domain_event_publisher import DomainEventPublisher
from src.domain.movie_session.movie_session import MovieSession
from src.domain.movie_session.movie_session_id import MovieSessionId
from src.usecase.movie_session.movie_session_extractor import MovieSessionExtractor
from src.usecase.movie_session.movie_session_persister import MovieSessionPersister


class InMemoryMovieSessionRepository(MovieSessionExtractor, MovieSessionPersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, movie_session_id: MovieSessionId) -> Union[MovieSession, None]:
        return self.__storage.get(movie_session_id)

    def get_all(self) -> List[MovieSession]:
        return list(self.__storage.values())

    def save(self, movie_session: MovieSession) -> None:
        self.__eventPublisher.publish(movie_session.pop_events())
        self.__storage[movie_session.id] = movie_session
