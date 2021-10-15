from typing import List, Dict, Optional

from src.common.event.domain_event_publisher import DomainEventPublisher
from src.folder_scan.domain.file_info import FileInfo
from src.folder_scan.domain.file_info_id import FileInfoId
from src.folder_scan.usecase.file_info_extractor import FileInfoExtractor
from src.folder_scan.usecase.file_info_persister import FileInfoPersister


class InMemoryFileInfoRepository(FileInfoExtractor, FileInfoPersister):
    __eventPublisher: DomainEventPublisher
    __storage: Dict = {}

    def __init__(self, event_publisher: DomainEventPublisher):
        self.__eventPublisher = event_publisher

    def get_by_id(self, file_info_id: FileInfoId) -> Optional[FileInfo]:
        return self.__storage.get(file_info_id)

    def get_by_name(self, name: str) -> List[FileInfo]:
        matches: List[FileInfo] = []

        for file_info in list(self.__storage.values()):
            if file_info.name == name:
                matches.append(file_info)

        return matches

    def get_by_name_and_duration(self, name: str, duration: int) -> Optional[FileInfo]:
        for file_info in list(self.__storage.values()):
            if file_info.name == name and file_info.duration == duration:
                return file_info

        return None

    def get_all(self) -> List[FileInfo]:
        return list(self.__storage.values())

    def save(self, file_info: FileInfo) -> None:
        self.__eventPublisher.publish(file_info.pop_events())
        self.__storage[file_info.id] = file_info
