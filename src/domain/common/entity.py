from abc import ABC
from typing import List

from src.domain.common.event.event import Event


class Entity(ABC):
    __events: List[Event]

    def add_event(self, event: Event) -> None:
        self.__events.append(event)

    def pop_events(self) -> List[Event]:
        events = self.__events
        self.__events.clear()
        return events
