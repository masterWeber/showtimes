from typing import List, Union, Dict

from src.domain.common.event.domain_event_publisher import DomainEventPublisher
from src.domain.time_interval.time_interval import TimeInterval
from src.domain.time_interval.time_interval_id import TimeIntervalId
from src.usecase.time_interval.time_interval_extractor import TimeIntervalExtractor
from src.usecase.time_interval.time_interval_persister import TimeIntervalPersister


class InMemoryTimeIntervalRepository(TimeIntervalExtractor, TimeIntervalPersister):
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, time_interval_id: TimeIntervalId) -> Union[TimeInterval, None]:
        return self.__storage.get(time_interval_id)

    def get_all(self) -> List[TimeInterval]:
        return list(self.__storage.values())

    def save(self, time_interval: TimeInterval) -> None:
        self.__storage[time_interval.id] = time_interval
