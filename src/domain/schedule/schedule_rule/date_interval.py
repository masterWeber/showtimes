import datetime
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass(frozen=True)
class DateInterval:
    start: date
    end: date

    def date_list(self) -> List[date]:
        return [
            self.start + datetime.timedelta(days=x)
            for x in
            range(0, (self.end - self.start).days + 1)
        ]
