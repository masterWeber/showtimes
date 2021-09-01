from abc import ABC, abstractmethod

from src.domain.schedule.schedule import Schedule


class SchedulePersister(ABC):

    @abstractmethod
    def save(self, schedule: Schedule) -> None:
        pass
