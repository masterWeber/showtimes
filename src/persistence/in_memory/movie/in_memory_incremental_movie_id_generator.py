from src.domain.movie.movie_id import MovieId
from src.domain.movie.movie_id_generator import MovieIdGenerator


class InMemoryIncrementalMovieIdGenerator(MovieIdGenerator):
    __counter: int = 0

    def generate(self) -> MovieId:
        return MovieId(++self.__counter)
