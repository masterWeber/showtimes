from abc import ABC, abstractmethod
from typing import List

from src.domain.movie.movie import Movie
from src.domain.movie.movie_id import MovieId


class MovieExtractor(ABC):

    @abstractmethod
    def get_by_id(self, movie_id: MovieId) -> List[Movie]:
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass
