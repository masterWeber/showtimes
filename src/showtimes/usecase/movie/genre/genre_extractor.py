from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.movie.genre.genre import Genre
from src.showtimes.domain.movie.genre.genre_id import GenreId


class GenreExtractor(ABC):

    @abstractmethod
    def get_by_id(self, genre_id: GenreId) -> Optional[Genre]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Genre]:
        pass

    @abstractmethod
    def get_all(self) -> List[Genre]:
        pass
