from typing import List, Union, Dict

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.showtimes.domain.movie.rating.rating_type import RatingType
from src.showtimes.domain.movie.rating.rating_type_id import RatingTypeId
from src.showtimes.usecase.movie.rating.rating_type_extractor import RatingTypeExtractor
from src.showtimes.usecase.movie.rating.rating_type_persister import RatingTypePersister


class InMemoryRatingTypeRepository(RatingTypeExtractor, RatingTypePersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, rating_type_id: RatingTypeId) -> Union[RatingType, None]:
        return self.__storage.get(rating_type_id)

    def get_by_name(self, name: str) -> Union[RatingType, None]:
        for rating_type in list(self.__storage.values()):
            if rating_type.name == name:
                return rating_type

        return None

    def get_all(self) -> List[RatingType]:
        return list(self.__storage.values())

    def save(self, rating_type: RatingType) -> None:
        self.__eventPublisher.publish(rating_type.pop_events())
        self.__storage[rating_type.id] = rating_type
