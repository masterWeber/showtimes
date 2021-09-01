from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.movie.movie import Movie
from src.domain.movie.movie_id import MovieId


class MovieExtractor(ABC):

    @abstractmethod
    def get_by_id(self, movie_id: MovieId) -> Union[Movie, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass
