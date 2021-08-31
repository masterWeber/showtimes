from src.domain.common.entity_id import EntityId


class IntervalId(EntityId):
    def __init__(self, value: int) -> None:
        super().__init__(value)
