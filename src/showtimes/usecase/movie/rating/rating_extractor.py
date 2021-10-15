from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.movie.rating.rating import Rating
from src.showtimes.domain.movie.rating.rating_id import RatingId


class RatingExtractor(ABC):

    @abstractmethod
    def get_by_id(self, rating_id: RatingId) -> Optional[Rating]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Rating]:
        pass

    @abstractmethod
    def get_all(self) -> List[Rating]:
        pass
