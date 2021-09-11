from abc import ABC, abstractmethod

from src.folder_scan.domain.file_info import FileInfo


class FileInfoPersister(ABC):

    @abstractmethod
    def save(self, file_info: FileInfo) -> None:
        pass
