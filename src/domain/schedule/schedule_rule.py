from src.domain.schedule.day_rule import DayRule
from src.domain.schedule.weekday import Weekday


class ScheduleRule:
    __weekday: Weekday
    __day: DayRule

    def __init__(self, weekday: Weekday, day: DayRule) -> None:
        self.__weekday = weekday
        self.__day = day
