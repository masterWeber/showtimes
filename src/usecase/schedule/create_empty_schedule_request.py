from dataclasses import dataclass
from typing import List

from src.domain.schedule.schedule_rule import ScheduleRule


@dataclass(frozen=True)
class CreateScheduleRequest:
    name: str
    rules: List[ScheduleRule]
