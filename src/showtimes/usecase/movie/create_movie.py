from abc import ABC, abstractmethod

from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.usecase.movie.create_movie_request import CreateMovieRequest


class CreateMovie(ABC):

    @abstractmethod
    def execute(self, request: CreateMovieRequest) -> MovieId:
        pass
