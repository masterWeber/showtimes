from src.domain.common.event.domain_event_id import DomainEventId


class DomainEvent:
    __id: DomainEventId

    def __init__(self) -> None:
        self.__id = DomainEventId.generate()
