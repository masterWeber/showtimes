from abc import ABC, abstractmethod
from typing import Union, List

from src.showtimes.domain.movie.rating.rating_type import RatingType
from src.showtimes.domain.movie.rating.rating_type_id import RatingTypeId


class RatingTypeExtractor(ABC):

    @abstractmethod
    def get_by_id(self, rating_type_id: RatingTypeId) -> Union[RatingType, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Union[RatingType, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[RatingType]:
        pass
