from typing import List

from src.folder_scan.domain.file_info_id_generator import FileInfoIdGenerator
from src.folder_scan.domain.video_ext import VideoExt
from src.folder_scan.usecase.collect_info import CollectInfo
from src.folder_scan.usecase.collect_info_request import CollectInfoRequest
from src.folder_scan.domain.file_info import FileInfo
from pymediainfo import MediaInfo

from src.folder_scan.usecase.file_info_extractor import FileInfoExtractor
from src.folder_scan.usecase.file_info_persister import FileInfoPersister


class CollectInfoUseCase(CollectInfo):
    __id_generator: FileInfoIdGenerator
    __persister: FileInfoPersister
    __extractor: FileInfoExtractor

    def __init__(
            self,
            id_generator: FileInfoIdGenerator,
            persister: FileInfoPersister,
            extractor: FileInfoExtractor
    ) -> None:
        self.__id_generator = id_generator
        self.__persister = persister
        self.__extractor = extractor

    def execute(self, request: CollectInfoRequest) -> List[FileInfo]:
        collected_info = []

        for path in request.path_list:
            media_info = MediaInfo.parse(path)
            general_track = media_info.general_tracks[0]

            file_name = general_track.file_name
            file_ext = VideoExt(general_track.file_extension)
            file_size = general_track.file_size
            duration = int((general_track.duration / 1000) / 60)

            file_info = self.__extractor.get_by_name_and_duration(file_name, duration)
            if file_info is None:
                file_info = FileInfo.create(
                    self.__id_generator,
                    file_name,
                    file_ext,
                    file_size,
                    duration
                )

                self.__persister.save(file_info)

            collected_info.append(file_info)

        return collected_info
