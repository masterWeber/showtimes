from __future__ import annotations

import uuid
from datetime import datetime
from uuid import UUID

__SECRET__ = object()


class DomainEventId:
    __value: UUID
    __created: datetime

    def __init__(
            self,
            value: UUID,
            secret: object = None,
            created: datetime = datetime.now()
    ) -> None:
        if secret != __SECRET__:
            raise ValueError("Use `generate` instead.")

        self.__value = value
        self.__created = created

    @staticmethod
    def generate() -> DomainEventId:
        return DomainEventId(uuid.uuid1(), __SECRET__)
