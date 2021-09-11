from abc import ABC, abstractmethod

from src.showtimes.domain.movie_session.movie_session import MovieSession


class MovieSessionPersister(ABC):

    @abstractmethod
    def save(self, movie_session: MovieSession) -> None:
        pass
