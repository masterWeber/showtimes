from abc import ABC, abstractmethod

from src.showtimes.domain.movie.movie import Movie


class MoviePersister(ABC):

    @abstractmethod
    def save(self, movie: Movie) -> None:
        pass
