from enum import Flag, auto


class DayRuleType(Flag):
    EVERYONE = auto()
    RANGE = auto()
    NUMBER = auto()
