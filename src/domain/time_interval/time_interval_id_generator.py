from abc import ABC, abstractmethod

from src.domain.time_interval.time_interval_id import TimeIntervalId


class TimeIntervalIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> TimeIntervalId:
        pass
