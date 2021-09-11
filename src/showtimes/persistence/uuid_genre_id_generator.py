import uuid

from src.showtimes.domain.movie.genre.genre_id import GenreId
from src.showtimes.domain.movie.genre.genre_id_generator import GenreIdGenerator


class UUIDGenreIdGenerator(GenreIdGenerator):

    def generate(self) -> GenreId:
        return GenreId(str(uuid.uuid4()))
