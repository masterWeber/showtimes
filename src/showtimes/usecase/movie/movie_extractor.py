from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.movie.movie import Movie
from src.showtimes.domain.movie.movie_id import MovieId


class MovieExtractor(ABC):

    @abstractmethod
    def get_by_id(self, movie_id: MovieId) -> Optional[Movie]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> List[Movie]:
        pass

    @abstractmethod
    def get_by_name_and_duration(self, name: str, duration: int) -> Optional[Movie]:
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass
