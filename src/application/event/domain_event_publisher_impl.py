from typing import List, Dict

from src.application.event.domain_event_listener import DomainEventListener
from src.common.event.domain_event import DomainEvent
from src.common.event.domain_event_publisher import DomainEventPublisher


class DomainEventPublisherImpl(DomainEventPublisher):
    __listener_map: Dict[type, List[DomainEventListener]]

    def register_listener(self, listener: DomainEventListener) -> None:
        event_type = listener.event_type()
        self.__listener_map[event_type].append(listener)

    def publish(self, events: List[DomainEvent]) -> None:
        for event in events:
            listeners = self.__listener_map[event.__class__]
            if listeners is not None:
                self.__send_events(listeners, event)

    @staticmethod
    def __send_events(listeners: List[DomainEventListener], event: DomainEvent) -> None:
        for listener in listeners:
            listener.handle(event)
