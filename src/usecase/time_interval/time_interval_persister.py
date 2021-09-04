from abc import ABC, abstractmethod

from src.domain.time_interval.time_interval import TimeInterval


class TimeIntervalPersister(ABC):

    @abstractmethod
    def save(self, time_interval: TimeInterval) -> None:
        pass
