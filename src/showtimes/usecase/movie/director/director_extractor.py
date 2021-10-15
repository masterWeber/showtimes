from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.movie.director.director import Director
from src.showtimes.domain.movie.director.director_id import DirectorId


class DirectorExtractor(ABC):

    @abstractmethod
    def get_by_id(self, director_id: DirectorId) -> Optional[Director]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Director]:
        pass

    @abstractmethod
    def get_all(self) -> List[Director]:
        pass
