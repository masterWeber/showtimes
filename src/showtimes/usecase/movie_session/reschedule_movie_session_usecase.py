from src.showtimes.usecase.movie_session.movie_session_extractor import MovieSessionExtractor
from src.showtimes.usecase.movie_session.movie_session_persister import MovieSessionPersister
from src.showtimes.usecase.movie_session.reschedule_movie_session import RescheduleMovieSession
from src.showtimes.usecase.movie_session.reschedule_movie_session_request import RescheduleMovieSessionRequest
from src.showtimes.usecase.time_interval.time_interval_extractor import TimeIntervalExtractor


class RescheduleMovieSessionUseCase(RescheduleMovieSession):
    __movie_session_persister: MovieSessionPersister
    __time_interval_extractor: TimeIntervalExtractor
    __movie_session_extractor: MovieSessionExtractor

    def __init__(
            self,
            movie_session_persister: MovieSessionPersister,
            time_interval_extractor: TimeIntervalExtractor,
            movie_session_extractor: MovieSessionExtractor
    ) -> None:
        self.__movie_session_persister = movie_session_persister
        self.__time_interval_extractor = time_interval_extractor
        self.__movie_session_extractor = movie_session_extractor

    def execute(self, request: RescheduleMovieSessionRequest) -> None:
        time_interval = self.__time_interval_extractor.get_by_id(request.time_interval_id)
        if time_interval is None:
            raise ValueError('Time interval not found.')

        movie_session = self.__movie_session_extractor.get_by_id(request.movie_session_id)
        if movie_session is None:
            raise ValueError('Movie session not found.')

        movie_session.reschedule(time_interval)
        self.__movie_session_persister.save(movie_session)
