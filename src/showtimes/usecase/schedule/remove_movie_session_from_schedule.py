from abc import ABC, abstractmethod

from src.showtimes.usecase.schedule.remove_movie_session_from_schedule_request \
    import RemoveMovieSessionFromScheduleRequest


class RemoveMovieSessionFromSchedule(ABC):

    @abstractmethod
    def execute(self, request: RemoveMovieSessionFromScheduleRequest) -> None:
        pass
