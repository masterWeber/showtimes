from __future__ import annotations
from typing import List, Union

from src.common.entity import Entity
from src.showtimes.domain.movie.director.director import Director
from src.showtimes.domain.movie.genre.genre import Genre
from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.domain.movie.movie_id_generator import MovieIdGenerator
from src.showtimes.domain.movie.rating.rating import Rating


class Movie(Entity):
    __id: MovieId
    __name: str
    __duration: int
    __year: int
    __genres: List[Genre] = []
    __ratings: List[Rating] = []
    __description: Union[str, None]
    __director: Union[Director, None]
    __poster: Union[str, None]
    __trailer: Union[str, None]

    def __init__(
            self,
            id_: MovieId,
            name: str,
            duration: int,
    ) -> None:
        if not name.strip():
            raise ValueError("The `name` cannot be empty.")

        self.__id = id_
        self.__name = name
        self.__duration = duration

    @property
    def id(self) -> MovieId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int) -> None:
        self.__duration = duration

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        self.__year = year

    @property
    def ratings(self) -> List[Rating]:
        return self.__ratings

    @ratings.setter
    def ratings(self, ratings: List[Rating]) -> None:
        self.__ratings = ratings

    def add_rating(self, rating: Rating) -> None:
        self.__ratings.append(rating)

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: Union[str, None]) -> None:
        self.__description = description

    @property
    def genres(self) -> List[Genre]:
        return self.__genres

    @genres.setter
    def genres(self, genres: List[Genre]) -> None:
        self.__genres = genres

    def add_genre(self, genre: Genre) -> None:
        self.__genres.append(genre)

    @property
    def director(self) -> Union[Director, None]:
        return self.__director

    @director.setter
    def director(self, director: Union[Director, None]) -> None:
        self.__director = director

    @property
    def poster(self) -> Union[str, None]:
        return self.__poster

    @poster.setter
    def poster(self, poster: Union[str, None]) -> None:
        self.__poster = poster

    @property
    def trailer(self) -> Union[str, None]:
        return self.__trailer

    @trailer.setter
    def trailer(self, trailer: Union[str, None]) -> None:
        self.__trailer = trailer

    @staticmethod
    def create(
            id_generator: MovieIdGenerator,
            name: str,
            duration: int,
    ) -> Movie:
        return Movie(
            id_generator.generate(),
            name,
            duration
        )
