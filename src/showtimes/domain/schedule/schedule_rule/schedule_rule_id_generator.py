from abc import ABC, abstractmethod

from src.showtimes.domain.schedule.schedule_rule.schedule_rule_id import ScheduleRuleId


class ScheduleRuleIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> ScheduleRuleId:
        pass
