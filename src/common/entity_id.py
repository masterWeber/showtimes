from src.common.value_object import ValueObject


class EntityId(ValueObject):
    __value: str

    def __init__(self, value: str) -> None:
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value
