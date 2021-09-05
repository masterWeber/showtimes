from abc import ABC, abstractmethod

from src.domain.time_interval.time_interval import TimeInterval
from src.usecase.time_interval.create_time_interval_request import CreateTimeIntervalRequest


class CreateTimeInterval(ABC):

    @abstractmethod
    def execute(self, request: CreateTimeIntervalRequest) -> TimeInterval:
        pass
