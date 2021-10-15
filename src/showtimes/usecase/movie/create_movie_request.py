from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from src.showtimes.domain.movie.director.director_id import DirectorId
from src.showtimes.domain.movie.genre.genre_id import GenreId
from src.showtimes.domain.movie.rating.rating_id import RatingId


@dataclass(frozen=True)
class CreateMovieRequest:
    name: str
    duration: int
    year: Optional[int]
    genre_ids: List[GenreId]
    rating_ids: List[RatingId]
    description: Optional[str]
    director_id: Optional[DirectorId]
    poster: Optional[str]
    trailer: Optional[str]

    @staticmethod
    def from_(
            name: str,
            duration: int,
            year: Optional[int] = None,
            genre_ids: List[int] = [],
            rating_ids: List[int] = [],
            description: Optional[str] = None,
            director_id: Optional[str] = None,
            poster: Optional[str] = None,
            trailer: Optional[str] = None
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
