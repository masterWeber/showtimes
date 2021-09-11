from enum import Enum


class VideoExt(Enum):
    MKV = 'mkv'
    MP4 = 'mp4'
    M4V = 'm4v'
    AVI = 'avi'

    @staticmethod
    def list():
        return list(map(lambda e: e.value, VideoExt))
