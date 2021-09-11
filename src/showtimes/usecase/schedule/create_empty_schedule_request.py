from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import List

from src.showtimes.domain.schedule.schedule_rule.date_interval import DateInterval
from src.showtimes.domain.schedule.schedule_rule.schedule_rule import ScheduleRule


@dataclass(frozen=True)
class CreateScheduleRequest:
    name: str
    date_interval: DateInterval
    rules: List[ScheduleRule]

    @staticmethod
    def from_(
            name: str,
            date_start: date,
            date_end: date,
            rules: List[ScheduleRule]
    ) -> CreateScheduleRequest:
        return CreateScheduleRequest(
            name,
            DateInterval(date_start, date_end),
            rules
        )
