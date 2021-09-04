from src.usecase.movie.movie_extractor import MovieExtractor
from src.usecase.movie.remove_movie_from_session import RemoveMovieFromSession
from src.usecase.movie.remove_movie_from_session_request import RemoveMovieFromSessionRequest
from src.usecase.movie_session.movie_session_extractor import MovieSessionExtractor
from src.usecase.movie_session.movie_session_persister import MovieSessionPersister


class RemoveMovieFromSessionUseCase(RemoveMovieFromSession):
    __movie_session_persister: MovieSessionPersister
    __movie_session_extractor: MovieSessionExtractor

    def __init__(
            self,
            movie_session_persister: MovieSessionPersister,
            movie_session_extractor: MovieSessionExtractor
    ) -> None:
        self.__movie_session_persister = movie_session_persister
        self.__movie_session_extractor = movie_session_extractor

    def execute(self, request: RemoveMovieFromSessionRequest) -> None:
        movie_session = self.__movie_session_extractor.get_by_id(request.movie_session_id)
        if movie_session is None:
            raise ValueError('Movie session is not found.')

        movie_session.movie = None
        self.__movie_session_persister.save(movie_session)
