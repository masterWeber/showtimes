import uuid

from src.showtimes.domain.movie.director.director_id import DirectorId
from src.showtimes.domain.movie.director.director_id_generator import DirectorIdGenerator


class UUIDDirectorIdGenerator(DirectorIdGenerator):

    def generate(self) -> DirectorId:
        return DirectorId(str(uuid.uuid4()))
