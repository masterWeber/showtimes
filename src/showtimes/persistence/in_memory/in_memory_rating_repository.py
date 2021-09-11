from typing import List, Union, Dict

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.movie.rating.rating import Rating
from src.showtimes.domain.movie.rating.rating_id import RatingId
from src.showtimes.usecase.movie.rating.rating_extractor import RatingExtractor
from src.showtimes.usecase.movie.rating.rating_persister import RatingPersister


class InMemoryRatingRepository(RatingExtractor, RatingPersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, rating_id: RatingId) -> Union[Rating, None]:
        return self.__storage.get(rating_id)

    def get_by_name(self, name: str) -> Union[Rating, None]:
        for rating in list(self.__storage.values()):
            if rating.name == name:
                return rating

        return None

    def get_all(self) -> List[Rating]:
        return list(self.__storage.values())

    def save(self, rating: Rating) -> None:
        self.__eventPublisher.publish(rating.pop_events())
        self.__storage[rating.id] = rating
