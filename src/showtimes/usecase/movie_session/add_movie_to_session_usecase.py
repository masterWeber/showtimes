from src.showtimes.usecase.movie_session.add_movie_to_session import AddMovieToSession
from src.showtimes.usecase.movie_session.add_movie_to_session_request import AddMovieToSessionRequest
from src.showtimes.usecase.movie.movie_extractor import MovieExtractor
from src.showtimes.usecase.movie_session.movie_session_extractor import MovieSessionExtractor
from src.showtimes.usecase.movie_session.movie_session_persister import MovieSessionPersister


class AddMovieToSessionUseCase(AddMovieToSession):
    __movie_session_persister: MovieSessionPersister
    __movie_extractor: MovieExtractor
    __movie_session_extractor: MovieSessionExtractor

    def __init__(
            self,
            movie_session_persister: MovieSessionPersister,
            movie_extractor: MovieExtractor,
            movie_session_extractor: MovieSessionExtractor
    ) -> None:
        self.__movie_session_persister = movie_session_persister
        self.__movie_extractor = movie_extractor
        self.__movie_session_extractor = movie_session_extractor

    def execute(self, request: AddMovieToSessionRequest) -> None:
        movie = self.__movie_extractor.get_by_id(request.movie_id)
        if movie is None:
            raise ValueError('Movie not found.')

        movie_session = self.__movie_session_extractor.get_by_id(request.movie_session_id)
        if movie_session is None:
            raise ValueError('Movie session not found.')

        movie_session.movie = movie
        self.__movie_session_persister.save(movie_session)
