from abc import ABC, abstractmethod

from src.showtimes.domain.schedule.schedule_id import ScheduleId


class ScheduleIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> ScheduleId:
        pass
