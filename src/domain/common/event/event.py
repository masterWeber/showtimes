from src.domain.common.event.event_id import EventId


class Event:
    __id: EventId

    def __init__(self) -> None:
        self.__id = EventId.generate()
