from abc import ABC, abstractmethod

from src.showtimes.domain.time_interval.time_interval import TimeInterval
from src.showtimes.usecase.time_interval.create_time_interval_request import CreateTimeIntervalRequest


class CreateTimeInterval(ABC):

    @abstractmethod
    def execute(self, request: CreateTimeIntervalRequest) -> TimeInterval:
        pass
