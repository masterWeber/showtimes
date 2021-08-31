from abc import ABC


class EntityId(ABC):
    __value: int

    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value
