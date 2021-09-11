from abc import ABC, abstractmethod

from src.showtimes.domain.schedule.schedule import Schedule
from src.showtimes.usecase.schedule.create_empty_schedule_request import CreateScheduleRequest


class CreateSchedule(ABC):

    @abstractmethod
    def execute(self, request: CreateScheduleRequest) -> Schedule:
        pass
