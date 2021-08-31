from abc import ABC, abstractmethod

from src.domain.movie.genre_id import GenreId


class GenreIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> GenreId:
        pass
