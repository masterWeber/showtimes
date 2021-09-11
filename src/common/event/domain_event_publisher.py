from abc import ABC, abstractmethod
from typing import List

from src.common.event.domain_event import DomainEvent


class DomainEventPublisher(ABC):

    @abstractmethod
    def publish(self, events: List[DomainEvent]) -> None:
        pass
