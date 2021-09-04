from abc import ABC, abstractmethod

from src.domain.movie_session.movie_session_id import MovieSessionId
from src.usecase.movie_session.create_movie_session_request import CreateMovieSessionRequest


class CreateMovieSession(ABC):

    @abstractmethod
    def execute(self, request: CreateMovieSessionRequest) -> MovieSessionId:
        pass
