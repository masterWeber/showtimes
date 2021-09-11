from abc import ABC, abstractmethod
from typing import List, Union

from src.showtimes.domain.movie.movie import Movie
from src.showtimes.domain.movie.movie_id import MovieId


class MovieExtractor(ABC):

    @abstractmethod
    def get_by_id(self, movie_id: MovieId) -> Union[Movie, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> List[Movie]:
        pass

    @abstractmethod
    def get_by_name_and_duration(self, name: str, duration: int) -> Union[Movie, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass
