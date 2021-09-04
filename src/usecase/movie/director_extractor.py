from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.movie.director import Director
from src.domain.movie.director_id import DirectorId


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
