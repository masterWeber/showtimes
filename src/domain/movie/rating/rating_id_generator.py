from abc import ABC, abstractmethod

from src.domain.movie.rating.rating_id import RatingId


class RatingIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> RatingId:
        pass
