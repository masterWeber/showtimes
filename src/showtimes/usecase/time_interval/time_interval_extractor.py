from abc import ABC, abstractmethod
from typing import List, Union

from src.showtimes.domain.time_interval.time_interval import TimeInterval
from src.showtimes.domain.time_interval.time_interval_id import TimeIntervalId


class TimeIntervalExtractor(ABC):

    @abstractmethod
    def get_by_id(self, time_interval_id: TimeIntervalId) -> Union[TimeInterval, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[TimeInterval]:
        pass
