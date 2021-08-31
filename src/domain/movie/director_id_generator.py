from abc import ABC, abstractmethod

from src.domain.movie.director_id import DirectorId


class DirectorIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> DirectorId:
        pass
