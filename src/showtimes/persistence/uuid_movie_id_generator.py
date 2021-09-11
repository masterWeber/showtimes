import uuid

from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.domain.movie.movie_id_generator import MovieIdGenerator


class UUIDMovieIdGenerator(MovieIdGenerator):

    def generate(self) -> MovieId:
        return MovieId(str(uuid.uuid4()))
