from abc import ABC, abstractmethod

from src.showtimes.domain.movie.director.director_id import DirectorId


class DirectorIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> DirectorId:
        pass
