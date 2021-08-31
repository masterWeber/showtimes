from src.domain.common.value_object import ValueObject
from src.domain.schedule.day_rule_type import DayRuleType


class DayRule(ValueObject):
    MIN_DAY = 1
    MAX_DAY = 31

    __value: str
    __type: DayRuleType

    def __init__(self, value: str) -> None:
        self.__type = self.get_type_from(value)

        self.__assert_valid_value(value)
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    @property
    def type(self) -> DayRuleType:
        return self.__type

    @staticmethod
    def get_type_from(value: str) -> DayRuleType:
        if '*' == value:
            return DayRuleType.ANY

        if '-' in value:
            return DayRuleType.RANGE

        if value.isnumeric():
            return DayRuleType.NUMBER

        raise ValueError('Invalid value.')

    def __assert_valid_value(self, value: str) -> None:
        if self.type == DayRuleType.RANGE:
            start, end = value.split('-', 1)

            if start < end \
                    and self.MIN_DAY <= int(start) <= self.MAX_DAY \
                    and self.MIN_DAY <= int(end) <= self.MAX_DAY:
                return

        if self.type == DayRuleType.NUMBER \
                and self.MIN_DAY <= int(value) <= self.MAX_DAY:
            return

        raise ValueError('Invalid value.')
