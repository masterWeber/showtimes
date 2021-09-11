from abc import ABC, abstractmethod
from typing import List, Union

from src.folder_scan.domain.file_info import FileInfo
from src.folder_scan.domain.file_info_id import FileInfoId


class FileInfoExtractor(ABC):

    @abstractmethod
    def get_by_id(self, file_info_id: FileInfoId) -> Union[FileInfo, None]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Union[FileInfo, None]:
        pass

    @abstractmethod
    def get_by_name_and_duration(self, name: str, duration: int) -> Union[FileInfo, None]:
        pass

    @abstractmethod
    def get_all(self) -> List[FileInfo]:
        pass
