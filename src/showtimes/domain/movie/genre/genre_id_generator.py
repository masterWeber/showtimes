from abc import ABC, abstractmethod

from src.showtimes.domain.movie.genre.genre_id import GenreId


class GenreIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> GenreId:
        pass
