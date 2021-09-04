from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union

from src.domain.movie.director_id import DirectorId
from src.domain.movie.genre_id import GenreId
from src.domain.movie.rating.rating_id import RatingId


@dataclass(frozen=True)
class CreateMovieRequest:
    name: str
    duration: int
    year: int
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
            year: int,
            genre_ids: List[GenreId],
            rating_ids: List[RatingId],
            description: Union[str, None],
            director_id: Union[DirectorId, None],
            poster: Union[str, None],
            trailer: Union[str, None]
    ) -> CreateMovieRequest:
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
