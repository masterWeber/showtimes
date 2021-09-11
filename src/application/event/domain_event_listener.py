from abc import ABC, abstractmethod

from src.common.event.domain_event import DomainEvent


class DomainEventListener(ABC):

    @staticmethod
    @abstractmethod
    def event_type() -> type:
        pass

    @staticmethod
    @abstractmethod
    def handle(event: DomainEvent) -> None:
        pass
