from __future__ import annotations
from datetime import date
from typing import Union

from src.domain.common.entity import Entity
from src.domain.common.time_interval import TimeInterval
from src.domain.schedule.date_rule import DateRule
from src.domain.schedule.date_rule_type import DateRuleType
from src.domain.schedule.schedule_rule_id import ScheduleRuleId
from src.domain.schedule.schedule_rule_id_generator import ScheduleRuleIdGenerator
from src.domain.schedule.weekday import Weekday


class ScheduleRule(Entity):
    __id: ScheduleRuleId
    __time_interval: TimeInterval
    __date: DateRule
    __weekday: Union[Weekday, None]

    def __init__(
            self,
            id_: ScheduleRuleId,
            time_interval: TimeInterval,
            date_: DateRule,
            weekday: Union[Weekday, None] = None
    ) -> None:
        self.__id = id_
        self.__time_interval = time_interval
        self.__date = date_
        self.__weekday = weekday

    @property
    def id(self) -> ScheduleRuleId:
        return self.__id

    @property
    def time_interval(self) -> TimeInterval:
        return self.__time_interval

    @time_interval.setter
    def time_interval(self, time_interval: TimeInterval) -> None:
        self.__time_interval = time_interval

    @property
    def date(self) -> DateRule:
        return self.__date

    @date.setter
    def date(self, date_: DateRule) -> None:
        self.__date = date_

    @property
    def weekday(self) -> Union[Weekday, None]:
        return self.__weekday

    @weekday.setter
    def weekday(self, weekday: Weekday) -> None:
        self.__weekday = weekday

    @staticmethod
    def create(
            id_generator: ScheduleRuleIdGenerator,
            time_interval: TimeInterval,
            date_: DateRule,
            weekday: Union[Weekday, None] = None
    ) -> ScheduleRule:
        return ScheduleRule(
            id_generator.generate(),
            time_interval,
            date_,
            weekday
        )

    def match(self, date_: date) -> bool:
        is_match_date = self.__match_date(date_)
        is_match_weekday = self.__match_weekday(date_.weekday())

        return is_match_date and is_match_weekday

    def __match_date(self, date_: date) -> bool:
        if self.date.type == DateRuleType.EVERYONE:
            return True

        if self.date.type == DateRuleType.RANGE:
            start, end = self.date.value.split('-', 1)
            return int(start) <= date_.day <= int(end)

        if self.date.type == DateRuleType.NUMBER:
            return date_.day == int(self.date.value)

        return False

    def __match_weekday(self, weekday: int) -> bool:
        if self.weekday is not None:
            return int(self.weekday) == weekday

        return True
