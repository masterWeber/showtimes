from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ScanRequest:
    path: str

    @staticmethod
    def from_(path: str) -> ScanRequest:
        return ScanRequest(path)
