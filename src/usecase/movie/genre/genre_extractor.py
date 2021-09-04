from abc import ABC, abstractmethod
from typing import Union, List

from src.domain.movie.genre.genre import Genre
from src.domain.movie.genre.genre_id import GenreId


class GenreExtractor(ABC):

    @abstractmethod
    def get_by_id(self, genre_id: GenreId) -> Union[Genre, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Union[Genre, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Genre]:
        pass
