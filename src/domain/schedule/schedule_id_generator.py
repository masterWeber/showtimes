from abc import ABC, abstractmethod

from src.domain.schedule.schedule_id import MovieSessionId


class ScheduleIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> MovieSessionId:
        pass
