import uuid

from src.showtimes.domain.time_interval.time_interval_id import TimeIntervalId
from src.showtimes.domain.time_interval.time_interval_id_generator import TimeIntervalIdGenerator


class UUIDTimeIntervalIdGenerator(TimeIntervalIdGenerator):

    def generate(self) -> TimeIntervalId:
        return TimeIntervalId(str(uuid.uuid4()))
