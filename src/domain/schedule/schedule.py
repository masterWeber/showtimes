from __future__ import annotations
from typing import List

from src.domain.common.entity import Entity
from src.domain.movie_session.movie_session import MovieSession
from src.domain.movie_session.movie_session_id import MovieSessionId
from src.domain.schedule.date_interval import DateInterval
from src.domain.schedule.schedule_id import MovieSessionId
from src.domain.schedule.schedule_id_generator import ScheduleIdGenerator


class Schedule(Entity):
    __id: MovieSessionId
    __name: str
    __date_interval: DateInterval
    __movie_sessions: List[MovieSession]

    def __init__(
            self,
            id_: MovieSessionId,
            name: str,
            movie_sessions: List[MovieSession] = None
    ) -> None:
        self.__id = id_
        self.__name = name

        if movie_sessions is None:
            self.__movie_sessions = []
        else:
            self.__movie_sessions = movie_sessions

    @property
    def id(self) -> MovieSessionId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def movie_sessions(self) -> List[MovieSession]:
        return self.__movie_sessions

    @movie_sessions.setter
    def movie_sessions(self, movie_sessions: List[MovieSession]) -> None:
        self.__movie_sessions = movie_sessions

    def add_movie_session(self, movie_session: MovieSession) -> None:
        self.__movie_sessions.append(movie_session)

    def remove_movie_session(self, movie_session: MovieSession) -> None:
        self.__movie_sessions.remove(movie_session)

    @staticmethod
    def create(id_generator: ScheduleIdGenerator, name: str, ) -> Schedule:
        return Schedule(id_generator.generate(), name)
