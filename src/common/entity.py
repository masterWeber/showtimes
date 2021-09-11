from abc import ABC
from typing import List

from src.common.event.domain_event import DomainEvent


class Entity(ABC):
    __events: List[DomainEvent] = []

    def add_event(self, event: DomainEvent) -> None:
        self.__events.append(event)

    def pop_events(self) -> List[DomainEvent]:
        events = self.__events
        self.__events.clear()
        return events
