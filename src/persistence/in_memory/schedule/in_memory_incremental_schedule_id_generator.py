from src.domain.schedule.schedule_id import ScheduleId
from src.domain.schedule.schedule_id_generator import ScheduleIdGenerator


class InMemoryIncrementalScheduleIdGenerator(ScheduleIdGenerator):
    __counter: int = 0

    def generate(self) -> ScheduleId:
        return ScheduleId(++self.__counter)
