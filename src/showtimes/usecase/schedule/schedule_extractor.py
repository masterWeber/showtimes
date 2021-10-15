from abc import ABC, abstractmethod
from typing import List, Optional

from src.showtimes.domain.schedule.schedule import Schedule
from src.showtimes.domain.schedule.schedule_id import ScheduleId


class ScheduleExtractor(ABC):

    @abstractmethod
    def get_by_id(self, schedule_id: ScheduleId) -> Optional[Schedule]:
        pass

    @abstractmethod
    def get_all(self) -> List[Schedule]:
        pass
