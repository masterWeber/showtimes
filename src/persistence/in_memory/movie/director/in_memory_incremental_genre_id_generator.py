from src.domain.movie.genre.genre_id import GenreId
from src.domain.movie.genre.genre_id_generator import GenreIdGenerator


class InMemoryIncrementalRatingIdGenerator(GenreIdGenerator):
    __counter: int = 0

    def generate(self) -> GenreId:
        return GenreId(++self.__counter)
