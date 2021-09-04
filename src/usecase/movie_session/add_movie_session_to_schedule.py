from abc import ABC, abstractmethod

from src.domain.movie_session.movie_session_id import MovieSessionId
from src.usecase.movie_session.add_movie_session_to_schedule_request import AddMovieSessionToScheduleRequest


class AddMovieSessionToSchedule(ABC):

    @abstractmethod
    def execute(self, request: AddMovieSessionToScheduleRequest) -> None:
        pass
