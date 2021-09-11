from abc import ABC, abstractmethod

from src.showtimes.usecase.movie_session.add_movie_to_session_request import AddMovieToSessionRequest


class AddMovieToSession(ABC):

    @abstractmethod
    def execute(self, request: AddMovieToSessionRequest) -> None:
        pass
