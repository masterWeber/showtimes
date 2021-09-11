from abc import ABC, abstractmethod

from src.showtimes.domain.movie.director.director import Director


class DirectorPersister(ABC):

    @abstractmethod
    def save(self, director: Director) -> None:
        pass
