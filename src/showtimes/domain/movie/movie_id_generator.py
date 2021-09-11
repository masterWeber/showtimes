from abc import ABC, abstractmethod

from src.showtimes.domain.movie.movie_id import MovieId


class MovieIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> MovieId:
        pass
