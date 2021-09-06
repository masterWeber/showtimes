from src.domain.time_interval.time_interval_id import TimeIntervalId
from src.domain.time_interval.time_interval_id_generator import TimeIntervalIdGenerator


class InMemoryIncrementalTimeIntervalIdGenerator(TimeIntervalIdGenerator):
    __counter: int = 0

    def generate(self) -> TimeIntervalId:
        return TimeIntervalId(++self.__counter)
