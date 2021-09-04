from src.usecase.movie.movie_extractor import MovieExtractor
from src.usecase.movie.remove_movie_from_session import RemoveMovieFromSession
from src.usecase.movie.remove_movie_from_session_request import RemoveMovieFromSessionRequest
from src.usecase.movie_session.movie_session_extractor import MovieSessionExtractor
from src.usecase.movie_session.movie_session_persister import MovieSessionPersister
from src.usecase.movie_session.remove_movie_session_from_schedule_request import RemoveMovieSessionFromScheduleRequest
from src.usecase.schedule.schedule_extractor import ScheduleExtractor
from src.usecase.schedule.schedule_persister import SchedulePersister


class RemoveMovieSessionFromScheduleUseCase(RemoveMovieFromSession):
    __schedule_persister: SchedulePersister
    __schedule_extractor: ScheduleExtractor
    __movie_session_extractor: MovieSessionExtractor

    def __init__(
            self,
            schedule_persister: SchedulePersister,
            schedule_extractor: ScheduleExtractor,
            movie_session_extractor: MovieSessionExtractor
    ) -> None:
        self.__schedule_persister = schedule_persister
        self.__schedule_extractor = schedule_extractor
        self.__movie_session_extractor = movie_session_extractor

    def execute(self, request: RemoveMovieSessionFromScheduleRequest) -> None:
        schedule = self.__schedule_extractor.get_by_id(request.schedule_id)
        if schedule is None:
            raise ValueError('Schedule not found.')

        movie_session = self.__movie_session_extractor.get_by_id(request.movie_session_id)
        if movie_session is None:
            raise ValueError('Movie session not found.')

        schedule.remove_movie_session(movie_session)
        self.__schedule_persister.save(schedule)
