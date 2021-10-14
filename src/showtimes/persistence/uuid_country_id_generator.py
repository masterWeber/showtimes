import uuid

from src.showtimes.domain.movie.country.country_id import CountryId
from src.showtimes.domain.movie.country.country_id_generator import CountryIdGenerator


class UUIDCountryIdGenerator(CountryIdGenerator):

    def generate(self) -> CountryId:
        return CountryId(str(uuid.uuid4()))
