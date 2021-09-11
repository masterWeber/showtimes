from __future__ import annotations

from typing import Union

from src.common.entity import Entity
from src.folder_scan.domain.file_info_id import FileInfoId
from src.folder_scan.domain.file_info_id_generator import FileInfoIdGenerator
from src.folder_scan.domain.video_ext import VideoExt
from src.showtimes.domain.movie.movie_id import MovieId


class FileInfo(Entity):
    __id: FileInfoId
    __name: str
    __ext: VideoExt
    __size: int
    __duration: int
    __movie_id: Union[MovieId, None]

    def __init__(
            self,
            id_: FileInfoId,
            name: str,
            ext: VideoExt,
            size: int,
            duration: int,
            movie_id: Union[MovieId, None]
    ) -> None:
        self.__id = id_
        self.__name = name
        self.__ext = ext
        self.__size = size
        self.__duration = duration
        self.__movie_id = movie_id

    @property
    def id(self) -> FileInfoId:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def ext(self) -> VideoExt:
        return self.__ext

    @ext.setter
    def ext(self, ext: VideoExt) -> None:
        self.__ext = ext

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        self.__size = size

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int) -> None:
        self.__duration = duration

    @property
    def movie_id(self) -> Union[MovieId, None]:
        return self.__movie_id

    @movie_id.setter
    def movie_id(self, movie_id: Union[MovieId, None]) -> None:
        self.__movie_id = movie_id

    @staticmethod
    def create(
            id_generator: FileInfoIdGenerator,
            name: str,
            ext: VideoExt,
            size: int,
            duration: int,
            movie_id: Union[MovieId, None] = None
    ) -> FileInfo:
        return FileInfo(
            id_generator.generate(),
            name,
            ext,
            size,
            duration,
            movie_id
        )
