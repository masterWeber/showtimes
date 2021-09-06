from typing import List, Union, Dict

from src.domain.common.event.domain_event_publisher import DomainEventPublisher
from src.domain.schedule.schedule import Schedule
from src.domain.schedule.schedule_id import ScheduleId
from src.usecase.schedule.schedule_extractor import ScheduleExtractor
from src.usecase.schedule.schedule_persister import SchedulePersister


class InMemoryScheduleRepository(ScheduleExtractor, SchedulePersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, schedule_id: ScheduleId) -> Union[Schedule, None]:
        return self.__storage.get(schedule_id)

    def get_all(self) -> List[Schedule]:
        return list(self.__storage.values())

    def save(self, schedule: Schedule) -> None:
        self.__eventPublisher.publish(schedule.pop_events())
        self.__storage[schedule.id] = schedule
