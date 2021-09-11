from abc import ABC, abstractmethod

from src.folder_scan.domain.file_info_id import FileInfoId


class FileInfoIdGenerator(ABC):

    @abstractmethod
    def generate(self) -> FileInfoId:
        pass
