from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.movie_session.movie_session import MovieSession
from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId


class MovieSessionExtractor(ABC):

    @abstractmethod
    def get_by_id(self, movie_session_id: MovieSessionId) -> Optional[MovieSession]:
        pass

    @abstractmethod
    def get_all(self) -> List[MovieSession]:
        pass
