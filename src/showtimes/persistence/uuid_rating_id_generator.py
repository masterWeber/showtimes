import uuid

from src.showtimes.domain.movie.rating.rating_id import RatingId
from src.showtimes.domain.movie.rating.rating_id_generator import RatingIdGenerator


class UUIDRatingIdGenerator(RatingIdGenerator):

    def generate(self) -> RatingId:
        return RatingId(str(uuid.uuid4()))
