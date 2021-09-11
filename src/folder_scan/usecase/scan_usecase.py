import os
import re
from pathlib import Path
from typing import List

from src.folder_scan.domain.video_ext import VideoExt
from src.folder_scan.usecase.scan import Scan
from src.folder_scan.usecase.scan_request import ScanRequest


class ScanUseCase(Scan):

    def execute(self, request: ScanRequest) -> List[Path]:
        match = []
        pattern = re.compile(r'.+\.(' + '|'.join(VideoExt.list()) + r')', flags=re.IGNORECASE)

        for root, dirs, files in os.walk(request.path):
            for file in files:
                if pattern.match(file):
                    file_path = Path(root).joinpath(file)
                    match.append(file_path)

        return match
