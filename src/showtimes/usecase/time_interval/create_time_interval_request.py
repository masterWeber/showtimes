from __future__ import annotations

from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class CreateTimeIntervalRequest:
    time_start: time
    time_end: time

    @staticmethod
    def from_(
            time_start: time,
            time_end: time,
    ) -> CreateTimeIntervalRequest:
        return CreateTimeIntervalRequest(
            time_start,
            time_end
        )
