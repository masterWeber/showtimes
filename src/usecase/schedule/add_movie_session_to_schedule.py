from abc import ABC, abstractmethod

from src.usecase.schedule.add_movie_session_to_schedule_request import AddMovieSessionToScheduleRequest


class AddMovieSessionToSchedule(ABC):

    @abstractmethod
    def execute(self, request: AddMovieSessionToScheduleRequest) -> None:
        pass
