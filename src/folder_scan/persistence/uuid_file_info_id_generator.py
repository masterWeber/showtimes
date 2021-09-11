import uuid

from src.folder_scan.domain.file_info_id import FileInfoId
from src.folder_scan.domain.file_info_id_generator import FileInfoIdGenerator


class UUIDFileInfoIdGenerator(FileInfoIdGenerator):

    def generate(self) -> FileInfoId:
        return FileInfoId(str(uuid.uuid4()))
