from src.domain.movie_session.movie_session import MovieSession
from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator
from src.usecase.movie_session.movie_session_persister import MovieSessionPersister
from src.usecase.movie_session.add_movie_session_to_schedule import AddMovieSessionToSchedule
from src.usecase.movie_session.add_movie_session_to_schedule_request import AddMovieSessionToScheduleRequest
from src.usecase.time_interval.time_interval_extractor import TimeIntervalExtractor


class AddMovieSessionToScheduleUseCase(AddMovieSessionToSchedule):
    __movie_session_id_generator: MovieSessionIdGenerator
    __movie_session_persister: MovieSessionPersister
    __time_interval_extractor: TimeIntervalExtractor

    def __init__(
            self,
            movie_session_id_generator: MovieSessionIdGenerator,
            movie_session_persister: MovieSessionPersister,
            time_interval_extractor: TimeIntervalExtractor
    ) -> None:
        self.__movie_session_id_generator = movie_session_id_generator
        self.__movie_session_persister = movie_session_persister
        self.__time_interval_extractor = time_interval_extractor

    def execute(self, request: AddMovieSessionToScheduleRequest) -> MovieSessionId:
        time_interval = self.__time_interval_extractor.get_by_id(request.time_interval_id)

        movie_session = MovieSession.create(
            self.__movie_session_id_generator,
            time_interval,
            request.date
        )

        return movie_session.id
