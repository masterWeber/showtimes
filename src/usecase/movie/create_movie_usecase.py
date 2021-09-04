from src.domain.movie.movie import Movie
from src.domain.movie.movie_id import MovieId
from src.domain.movie.movie_id_generator import MovieIdGenerator
from src.usecase.movie.create_movie import CreateMovie
from src.usecase.movie.create_movie_request import CreateMovieRequest
from src.usecase.movie.director_extractor import DirectorExtractor
from src.usecase.movie.genre_extractor import GenreExtractor
from src.usecase.movie.movie_persister import MoviePersister
from src.usecase.movie.rating_extractor import RatingExtractor


class CreateMovieUseCase(CreateMovie):
    __movie_id_generator: MovieIdGenerator
    __movie_persister: MoviePersister
    __director_extractor: DirectorExtractor
    __genre_extractor: GenreExtractor
    __rating_extractor: RatingExtractor

    def execute(self, request: CreateMovieRequest) -> MovieId:
        movie = Movie.create(
            self.__movie_id_generator,
            request.name,
            request.duration,
            request.year
        )

        for genre_id in request.genre_ids:
            genre = self.__genre_extractor.get_by_id(genre_id)
            if genre is not None:
                movie.add_genre(genre)

        for rating_id in request.rating_ids:
            rating = self.__rating_extractor.get_by_id(rating_id)
            if rating is not None:
                movie.add_rating(rating)

        if request.director_id is not None:
            movie.director = self.__director_extractor.get_by_id(request.director_id)

        movie.poster = request.poster
        movie.poster = request.poster
        movie.trailer = request.trailer

        self.__movie_persister.save(movie)

        return movie.id
