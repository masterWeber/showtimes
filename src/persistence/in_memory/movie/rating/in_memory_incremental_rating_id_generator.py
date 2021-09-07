from src.domain.movie.rating.rating_id import RatingId
from src.domain.movie.rating.rating_id_generator import RatingIdGenerator


class InMemoryIncrementalRatingIdGenerator(RatingIdGenerator):
    __counter: int = 0

    def generate(self) -> RatingId:
        return RatingId(++self.__counter)
