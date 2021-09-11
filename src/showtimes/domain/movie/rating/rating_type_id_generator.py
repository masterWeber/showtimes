from abc import ABC, abstractmethod

from src.showtimes.domain.movie.rating.rating_type_id import RatingTypeId


class RatingTypeIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> RatingTypeId:
        pass
