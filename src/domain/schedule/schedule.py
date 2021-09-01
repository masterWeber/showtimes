from __future__ import annotations
from typing import List

from src.domain.common.entity import Entity
from src.domain.movie_session.movie_session import MovieSession
from src.domain.schedule.date_interval import DateInterval
from src.domain.schedule.schedule_id import ScheduleId
from src.domain.schedule.schedule_id_generator import ScheduleIdGenerator


class Schedule(Entity):
    __id: ScheduleId
    __name: str
    __date_interval: DateInterval
    __movie_sessions: List[MovieSession]

    def __init__(
            self,
            id_: ScheduleId,
            name: str,
            date_interval: DateInterval,
            movie_sessions: List[MovieSession] = None
    ) -> None:
        self.__id = id_
        self.__name = name
        self.__date_interval = date_interval

        if movie_sessions is None:
            self.__movie_sessions = []
        else:
            self.__movie_sessions = movie_sessions

    @property
    def id(self) -> ScheduleId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def date_interval(self) -> DateInterval:
        return self.__date_interval

    @date_interval.setter
    def date_interval(self, date_interval: DateInterval) -> None:
        self.__date_interval = date_interval

    @property
    def movie_sessions(self) -> List[MovieSession]:
        return self.__movie_sessions

    @movie_sessions.setter
    def movie_sessions(self, movie_sessions: List[MovieSession]) -> None:
        self.__movie_sessions = movie_sessions

    def add_movie_session(self, movie_session: MovieSession) -> None:
        self.__movie_sessions.append(movie_session)

    @staticmethod
    def create(
            id_generator: ScheduleIdGenerator,
            name: str,
            date_interval: DateInterval
    ) -> Schedule:
        return Schedule(id_generator.generate(), name, date_interval)
