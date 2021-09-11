import uuid

from src.showtimes.domain.movie_session.movie_session_id import MovieSessionId
from src.showtimes.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator


class UUIDMovieSessionIdGenerator(MovieSessionIdGenerator):

    def generate(self) -> MovieSessionId:
        return MovieSessionId(str(uuid.uuid4()))
