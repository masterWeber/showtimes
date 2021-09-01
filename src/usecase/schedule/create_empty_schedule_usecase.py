from typing import List

from src.domain.movie_session.movie_session import MovieSession
from src.domain.schedule.schedule import Schedule
from src.domain.schedule.schedule_id_generator import ScheduleIdGenerator
from src.domain.schedule.schedule_rule import ScheduleRule
from src.usecase.schedule.create_schedule import CreateSchedule
from src.usecase.schedule.create_empty_schedule_request import CreateScheduleRequest
from src.usecase.schedule.schedule_persister import SchedulePersister


class CreateEmptyScheduleUseCase(CreateSchedule):
    __schedule_persister: SchedulePersister
    __id_generator: ScheduleIdGenerator

    def __init__(
            self,
            schedule_persister: SchedulePersister,
            id_generator: ScheduleIdGenerator
    ) -> None:
        self.__schedule_persister = schedule_persister
        self.__id_generator = id_generator

    def execute(self, request: CreateScheduleRequest) -> Schedule:
        schedule = Schedule.create(
            self.__id_generator,
            request.name,
        )

        movie_sessions: List[MovieSession] = []

        for rule in request.rules:
            movie_sessions.extend(self.__create_movie_session(rule))

        movie_sessions.sort(key=lambda ms: ms.date)

        for movie_session in movie_sessions:
            schedule.add_movie_session(movie_session)

        self.__schedule_persister.save(schedule)

        return schedule

    def __create_movie_session(self, rule: ScheduleRule) -> List[MovieSession]:
        # TODO: create movie sessions by rule
        return []
