from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class CollectInfoRequest:
    path_list: List[Path]

    @staticmethod
    def from_(path_list: List[Path]) -> CollectInfoRequest:
        return CollectInfoRequest(path_list)
