from src.showtimes.domain.time_interval.time_interval import TimeInterval
from src.showtimes.domain.time_interval.time_interval_id_generator import TimeIntervalIdGenerator
from src.showtimes.usecase.time_interval.create_time_interval import CreateTimeInterval
from src.showtimes.usecase.time_interval.create_time_interval_request import CreateTimeIntervalRequest
from src.showtimes.usecase.time_interval.time_interval_persister import TimeIntervalPersister


class CreateTimeIntervalUseCase(CreateTimeInterval):
    __persister: TimeIntervalPersister
    __id_generator: TimeIntervalIdGenerator

    def __init__(
            self,
            time_interval_persister: TimeIntervalPersister,
            time_interval_id_generator: TimeIntervalIdGenerator,
    ) -> None:
        self.__persister = time_interval_persister
        self.__id_generator = time_interval_id_generator

    def execute(self, request: CreateTimeIntervalRequest) -> TimeInterval:
        time_interval = TimeInterval.create(
            self.__id_generator,
            request.time_start,
            request.time_end
        )

        self.__persister.save(time_interval)

        return time_interval
