from typing import List, Dict, Optional

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.schedule.schedule import Schedule
from src.showtimes.domain.schedule.schedule_id import ScheduleId
from src.showtimes.usecase.schedule.schedule_extractor import ScheduleExtractor
from src.showtimes.usecase.schedule.schedule_persister import SchedulePersister


class InMemoryScheduleRepository(ScheduleExtractor, SchedulePersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, schedule_id: ScheduleId) -> Optional[Schedule]:
        return self.__storage.get(schedule_id)

    def get_all(self) -> List[Schedule]:
        return list(self.__storage.values())

    def save(self, schedule: Schedule) -> None:
        self.__eventPublisher.publish(schedule.pop_events())
        self.__storage[schedule.id] = schedule
