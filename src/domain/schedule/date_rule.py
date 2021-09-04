from __future__ import annotations

from src.domain.common.value_object import ValueObject
from src.domain.schedule.date_rule_type import DateRuleType


class DateRule(ValueObject):
    MIN_DAY = 1
    MAX_DAY = 31

    __value: str
    __type: DateRuleType

    def __init__(self, value: str, type_: DateRuleType) -> None:
        self.__assert_valid_value(value, type_)

        self.__value = value
        self.__type = type_

    @property
    def value(self) -> str:
        return self.__value

    @property
    def type(self) -> DateRuleType:
        return self.__type

    def __assert_valid_value(self, value: str, type_: DateRuleType) -> None:
        if type_ == DateRuleType.EVERYONE \
                and value == '*':
            return

        if type_ == DateRuleType.RANGE:
            start, end = value.split('-', 1)

            if start < end \
                    and self.MIN_DAY <= int(start) <= self.MAX_DAY \
                    and self.MIN_DAY <= int(end) <= self.MAX_DAY:
                return

        if type_ == DateRuleType.NUMBER \
                and self.MIN_DAY <= int(value) <= self.MAX_DAY:
            return

        raise ValueError('Invalid value.')

    @staticmethod
    def __get_type_from(value: str) -> DateRuleType:
        if '*' == value:
            return DateRuleType.EVERYONE

        if '-' in value:
            return DateRuleType.RANGE

        if value.isnumeric():
            return DateRuleType.NUMBER

        raise ValueError('Invalid value.')

    @staticmethod
    def from_(value: str) -> DateRule:
        type_ = DateRule.__get_type_from(value)

        return DateRule(value, type_)
