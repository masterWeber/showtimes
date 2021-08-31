from abc import ABC, abstractmethod
from typing import List

from src.domain.common.event.event import Event


class EventPublisher(ABC):

    @abstractmethod
    def publish(self, events: List[Event]) -> None:
        pass
