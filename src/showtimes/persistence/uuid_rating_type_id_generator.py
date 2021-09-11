import uuid

from src.showtimes.domain.movie.rating.rating_type_id import RatingTypeId
from src.showtimes.domain.movie.rating.rating_type_id_generator import RatingTypeIdGenerator


class UUIDRatingTypeIdGenerator(RatingTypeIdGenerator):

    def generate(self) -> RatingTypeId:
        return RatingTypeId(str(uuid.uuid4()))
