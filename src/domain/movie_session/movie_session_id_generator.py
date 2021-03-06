from abc import ABC, abstractmethod

from src.domain.movie_session.movie_session_id import MovieSessionId


class MovieSessionIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> MovieSessionId:
        pass
