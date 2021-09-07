from abc import ABC, abstractmethod
from typing import List, Union

from src.domain.schedule.schedule import Schedule
from src.domain.schedule.schedule_id import ScheduleId


class ScheduleExtractor(ABC):

    @abstractmethod
    def get_by_id(self, schedule_id: ScheduleId) -> Union[Schedule, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Schedule]:
        pass
