from src.domain.common.entity import Entity
from src.domain.schedule.day_rule import DayRule
from src.domain.schedule.schedule_rule_id import ScheduleRuleId
from src.domain.schedule.weekday import Weekday


class ScheduleRule(Entity):
    __id: ScheduleRuleId
    __weekday: Weekday
    __day: DayRule

    def __init__(self, id_: ScheduleRuleId, weekday: Weekday, day: DayRule) -> None:
        self.__id = id_
        self.__weekday = weekday
        self.__day = day

    @property
    def weekday(self) -> Weekday:
        return self.__weekday

    @weekday.setter
    def weekday(self, weekday: Weekday) -> None:
        self.__weekday = weekday

    @property
    def day(self) -> DayRule:
        return self.__day

    @day.setter
    def day(self, day: DayRule) -> None:
        self.__day = day
