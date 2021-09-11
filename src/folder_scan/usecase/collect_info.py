from abc import ABC, abstractmethod
from typing import List

from src.folder_scan.domain.file_info import FileInfo
from src.folder_scan.usecase.collect_info_request import CollectInfoRequest


class CollectInfo(ABC):

    @abstractmethod
    def execute(self, request: CollectInfoRequest) -> List[FileInfo]:
        pass
