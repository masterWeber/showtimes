from typing import List

from src.showtimes.domain.movie_session.movie_session import MovieSession
from src.showtimes.domain.movie_session.movie_session_id_generator import MovieSessionIdGenerator
from src.showtimes.domain.schedule.schedule_rule.date_interval import DateInterval
from src.showtimes.domain.schedule.schedule import Schedule
from src.showtimes.domain.schedule.schedule_id_generator import ScheduleIdGenerator
from src.showtimes.domain.schedule.schedule_rule.schedule_rule import ScheduleRule
from src.showtimes.usecase.schedule.create_schedule import CreateSchedule
from src.showtimes.usecase.schedule.create_empty_schedule_request import CreateScheduleRequest
from src.showtimes.usecase.schedule.schedule_persister import SchedulePersister


class CreateEmptyScheduleUseCase(CreateSchedule):
    __schedule_persister: SchedulePersister
    __schedule_id_generator: ScheduleIdGenerator
    __movie_session_id_generator: MovieSessionIdGenerator

    def __init__(
            self,
            schedule_persister: SchedulePersister,
            schedule_id_generator: ScheduleIdGenerator,
            movie_session_id_generator: MovieSessionIdGenerator
    ) -> None:
        self.__schedule_persister = schedule_persister
        self.__schedule_id_generator = schedule_id_generator
        self.__movie_session_id_generator = movie_session_id_generator

    def execute(self, request: CreateScheduleRequest) -> Schedule:
        schedule = Schedule.create(self.__schedule_id_generator, request.name)
        schedule.movie_sessions = self.__create_movie_sessions(
            request.rules, request.date_interval
        )

        self.__schedule_persister.save(schedule)

        return schedule

    def __create_movie_sessions(
            self,
            rules: List[ScheduleRule],
            date_interval: DateInterval
    ) -> List[MovieSession]:
        movie_sessions: List[MovieSession] = []

        date_list = date_interval.date_list()

        for date in date_list:
            for rule in rules:
                if rule.match(date):
                    movie_session = MovieSession.create(
                        self.__movie_session_id_generator,
                        rule.time_interval,
                        date
                    )
                    movie_sessions.append(movie_session)

        return sorted(movie_sessions, key=lambda ms: ms.date)
