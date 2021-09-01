from src.domain.common.value_object import ValueObject


class EntityId(ValueObject):
    __value: int

    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value
