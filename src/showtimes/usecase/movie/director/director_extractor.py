from abc import ABC, abstractmethod
from typing import List, Union

from src.showtimes.domain.movie.director.director import Director
from src.showtimes.domain.movie.director.director_id import DirectorId


class DirectorExtractor(ABC):

    @abstractmethod
    def get_by_id(self, director_id: DirectorId) -> Union[Director, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Union[Director, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Director]:
        pass
