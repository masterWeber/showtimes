from abc import ABC, abstractmethod

from src.domain.movie.rating.rating import Rating


class RatingPersister(ABC):

    @abstractmethod
    def save(self, rating: Rating) -> None:
        pass
