from abc import abstractmethod, ABC
from pathlib import Path
from typing import List

from src.folder_scan.usecase.scan_request import ScanRequest


class Scan(ABC):

    @abstractmethod
    def execute(self, request: ScanRequest) -> List[Path]:
        pass
