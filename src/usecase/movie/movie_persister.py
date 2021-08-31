from abc import ABC, abstractmethod

from src.domain.movie.movie import Movie


class MoviePersister(ABC):

    @abstractmethod
    def save(self, movie: Movie) -> bool:
        pass
