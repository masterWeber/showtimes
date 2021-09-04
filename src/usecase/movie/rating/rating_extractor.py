from abc import ABC, abstractmethod
from typing import Union, List

from src.domain.movie.rating.rating import Rating
from src.domain.movie.rating.rating_id import RatingId


class RatingExtractor(ABC):

    @abstractmethod
    def get_by_id(self, rating_id: RatingId) -> Union[Rating, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Union[Rating, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Rating]:
        pass
