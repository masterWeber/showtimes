from abc import ABC, abstractmethod
from typing import List, Optional

from src.folder_scan.domain.file_info import FileInfo
from src.folder_scan.domain.file_info_id import FileInfoId


class FileInfoExtractor(ABC):

    @abstractmethod
    def get_by_id(self, file_info_id: FileInfoId) -> Optional[FileInfo]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[FileInfo]:
        pass

    @abstractmethod
    def get_by_name_and_duration(self, name: str, duration: int) -> Optional[FileInfo]:
        pass

    @abstractmethod
    def get_all(self) -> List[FileInfo]:
        pass
