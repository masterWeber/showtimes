from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union

from src.showtimes.domain.movie.director.director_id import DirectorId
from src.showtimes.domain.movie.genre.genre_id import GenreId
from src.showtimes.domain.movie.rating.rating_id import RatingId


@dataclass(frozen=True)
class CreateMovieRequest:
    name: str
    duration: int
    year: Union[int, None]
    genre_ids: List[GenreId]
    rating_ids: List[RatingId]
    description: Union[str, None]
    director_id: Union[DirectorId, None]
    poster: Union[str, None]
    trailer: Union[str, None]

    @staticmethod
    def from_(
            name: str,
            duration: int,
            year: Union[int, None] = None,
            genre_ids: List[int] = [],
            rating_ids: List[int] = [],
            description: Union[str, None] = None,
            director_id: Union[str, None] = None,
            poster: Union[str, None] = None,
            trailer: Union[str, None] = None
    ) -> CreateMovieRequest:
        director_id = None if director_id is None else DirectorId(director_id)

        rating_ids = list(map(lambda rating_id: RatingId(rating_id), rating_ids))
        genre_ids = list(map(lambda genre_id: GenreId(genre_id), genre_ids))

        return CreateMovieRequest(
            name,
            duration,
            year,
            genre_ids,
            rating_ids,
            description,
            director_id,
            poster,
            trailer
        )
