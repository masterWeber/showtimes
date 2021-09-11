from __future__ import annotations
from datetime import time, datetime, date

from src.common.entity import Entity
from src.showtimes.domain.time_interval.time_interval_id import TimeIntervalId
from src.showtimes.domain.time_interval.time_interval_id_generator import TimeIntervalIdGenerator


class TimeInterval(Entity):
    __id: TimeIntervalId
    __start: time
    __end: time

    def __init__(self, id_: TimeIntervalId, start: time, end: time) -> None:
        self.__id = id_
        self.__start = start
        self.__end = end

    @property
    def id(self) -> TimeIntervalId:
        return self.__id

    @property
    def start(self) -> time:
        return self.__start

    @start.setter
    def start(self, start: time) -> None:
        self.__start = start

    @property
    def end(self) -> time:
        return self.__end

    @end.setter
    def end(self, end: time) -> None:
        self.__end = end

    @staticmethod
    def create(id_generator: TimeIntervalIdGenerator, start: time, end: time) -> TimeInterval:
        return TimeInterval(id_generator.generate(), start, end)

    @property
    def duration(self) -> int:
        start = datetime.combine(date.min, self.start)
        end = datetime.combine(date.min, self.end)
        timedelta = end - start
        return int(timedelta.total_seconds() // 60)
