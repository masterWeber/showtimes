from abc import ABC, abstractmethod

from src.domain.movie.genre.genre import Genre


class GenrePersister(ABC):

    @abstractmethod
    def save(self, genre: Genre) -> None:
        pass
