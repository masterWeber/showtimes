from abc import ABC, abstractmethod

from src.domain.schedule.schedule_rule_id import ScheduleRuleId


class ScheduleRuleIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> ScheduleRuleId:
        pass
