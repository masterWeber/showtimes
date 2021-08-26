from __future__ import annotations
from datetime import time, datetime, date

from src.domain.movie_session.interval_id import IntervalId


class Interval:
    __id: IntervalId
    __start: time
    __end: time

    def __init__(self, id_: IntervalId, start: time, end: time):
        self.__id = id_
        self.__start = start
        self.__end = end

    @property
    def id(self) -> IntervalId:
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

    @property
    def duration(self) -> int:
        start = datetime.combine(date.min, self.start)
        end = datetime.combine(date.min, self.end)
        timedelta = end - start
        return int(timedelta.total_seconds() // 60)
