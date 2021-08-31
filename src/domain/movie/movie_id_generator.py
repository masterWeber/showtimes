from abc import ABC, abstractmethod

from src.domain.movie.movie_id import MovieId


class MovieIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> MovieId:
        pass
