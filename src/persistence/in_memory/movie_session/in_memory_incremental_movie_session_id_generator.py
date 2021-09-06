from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator


class InMemoryIncrementalMovieSessionIdGenerator(MovieSessionIdGenerator):
    __counter: int = 0

    def generate(self) -> MovieSessionId:
        return MovieSessionId(++self.__counter)
