from abc import ABC, abstractmethod

from src.domain.movie_session.interval_id import IntervalId


class IntervalIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> IntervalId:
        pass
