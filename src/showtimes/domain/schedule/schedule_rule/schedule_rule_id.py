from src.common.entity_id import EntityId


class ScheduleRuleId(EntityId):
    def __init__(self, value: str) -> None:
        super().__init__(value)
