import uuid

from src.showtimes.domain.schedule.schedule_id import ScheduleId
from src.showtimes.domain.schedule.schedule_id_generator import ScheduleIdGenerator


class UUIDScheduleIdGenerator(ScheduleIdGenerator):

    def generate(self) -> ScheduleId:
        return ScheduleId(str(uuid.uuid4()))
