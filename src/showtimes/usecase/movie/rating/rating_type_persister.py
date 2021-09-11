from abc import ABC, abstractmethod

from src.showtimes.domain.movie.rating.rating_type import RatingType


class RatingTypePersister(ABC):

    @abstractmethod
    def save(self, rating_type: RatingType) -> None:
        pass
