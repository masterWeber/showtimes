from abc import ABC, abstractmethod

from src.usecase.movie_session.reschedule_movie_session_request import RescheduleMovieSessionRequest


class RescheduleMovieSession(ABC):

    @abstractmethod
    def execute(self, request: RescheduleMovieSessionRequest) -> None:
        pass
