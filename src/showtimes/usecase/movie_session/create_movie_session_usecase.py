from src.showtimes.domain.movie_session.movie_session import MovieSession
from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId
from src.showtimes.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator
from src.showtimes.usecase.movie.movie_extractor import MovieExtractor
from src.showtimes.usecase.movie_session.create_movie_session import CreateMovieSession
from src.showtimes.usecase.movie_session.create_movie_session_request import CreateMovieSessionRequest
from src.showtimes.usecase.movie_session.movie_session_persister import MovieSessionPersister
from src.showtimes.usecase.time_interval.time_interval_extractor import TimeIntervalExtractor


class CreateMovieSessionUseCase(CreateMovieSession):
    __movie_session_id_generator: MovieSessionIdGenerator
    __movie_session_persister: MovieSessionPersister
    __time_interval_extractor: TimeIntervalExtractor
    __movie_extractor: MovieExtractor

    def __init__(
            self,
            movie_session_id_generator: MovieSessionIdGenerator,
            movie_session_persister: MovieSessionPersister,
            time_interval_extractor: TimeIntervalExtractor,
            movie_extractor: MovieExtractor,
    ) -> None:
        self.__movie_session_id_generator = movie_session_id_generator
        self.__movie_session_persister = movie_session_persister
        self.__time_interval_extractor = time_interval_extractor
        self.__movie_extractor = movie_extractor

    def execute(self, request: CreateMovieSessionRequest) -> MovieSessionId:
        time_interval = self.__time_interval_extractor.get_by_id(request.time_interval_id)
        if time_interval is None:
            raise ValueError('Time interval not found.')

        movie_session = MovieSession.create(
            self.__movie_session_id_generator,
            time_interval,
            request.date
        )

        if request.movie_id is not None:
            movie = self.__movie_extractor.get_by_id(request.movie_id)
            if movie is None:
                raise ValueError('Movie interval not found.')

            movie_session.movie = movie

        self.__movie_session_persister.save(movie_session)
        return movie_session.id
