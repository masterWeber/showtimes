from abc import ABC, abstractmethod

from src.usecase.movie.remove_movie_from_session_request import RemoveMovieFromSessionRequest


class RemoveMovieFromSession(ABC):

    @abstractmethod
    def execute(self, request: RemoveMovieFromSessionRequest) -> None:
        pass
