from src.domain.common.entity_id import EntityId


class RatingTypeId(EntityId):
    def __init__(self, value: int) -> None:
        super().__init__(value)
