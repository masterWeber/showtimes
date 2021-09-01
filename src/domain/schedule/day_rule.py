from __future__ import annotations

from src.domain.common.value_object import ValueObject
from src.domain.schedule.day_rule_type import DayRuleType


class DayRule(ValueObject):
    MIN_DAY = 1
    MAX_DAY = 31

    __value: str
    __type: DayRuleType

    def __init__(self, value: str, type_: DayRuleType) -> None:
        self.__assert_valid_value(value, type_)

        self.__value = value
        self.__type = type_

    @property
    def value(self) -> str:
        return self.__value

    @property
    def type(self) -> DayRuleType:
        return self.__type

    def __assert_valid_value(self, value: str, type_: DayRuleType) -> None:
        if type_ == DayRuleType.EVERYONE \
                and value == '*':
            return

        if type_ == DayRuleType.RANGE:
            start, end = value.split('-', 1)

            if start < end \
                    and self.MIN_DAY <= int(start) <= self.MAX_DAY \
                    and self.MIN_DAY <= int(end) <= self.MAX_DAY:
                return

        if type_ == DayRuleType.NUMBER \
                and self.MIN_DAY <= int(value) <= self.MAX_DAY:
            return

        raise ValueError('Invalid value.')

    @staticmethod
    def __get_type_from(value: str) -> DayRuleType:
        if '*' == value:
            return DayRuleType.EVERYONE

        if '-' in value:
            return DayRuleType.RANGE

        if value.isnumeric():
            return DayRuleType.NUMBER

        raise ValueError('Invalid value.')

    @staticmethod
    def from_(value: str) -> DayRule:
        type_ = DayRule.__get_type_from(value)

        return DayRule(value, type_)
