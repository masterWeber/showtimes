from enum import Flag, auto


class DayRuleType(Flag):
    ANY = auto()
    RANGE = auto()
    NUMBER = auto()
