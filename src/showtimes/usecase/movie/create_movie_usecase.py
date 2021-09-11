from src.showtimes.domain.movie.movie import Movie
from src.showtimes.domain.movie.movie_id import MovieId
from src.showtimes.domain.movie.movie_id_generator import MovieIdGenerator
from src.showtimes.usecase.movie.create_movie import CreateMovie
from src.showtimes.usecase.movie.create_movie_request import CreateMovieRequest
from src.showtimes.usecase.movie.director.director_extractor import DirectorExtractor
from src.showtimes.usecase.movie.genre.genre_extractor import GenreExtractor
from src.showtimes.usecase.movie.movie_persister import MoviePersister
from src.showtimes.usecase.movie.rating.rating_extractor import RatingExtractor


class CreateMovieUseCase(CreateMovie):
    __movie_id_generator: MovieIdGenerator
    __movie_persister: MoviePersister
    __director_extractor: DirectorExtractor
    __genre_extractor: GenreExtractor
    __rating_extractor: RatingExtractor

    def __init__(
            self,
            movie_id_generator: MovieIdGenerator,
            movie_persister: MoviePersister,
            director_extractor: DirectorExtractor,
            genre_extractor: GenreExtractor,
            rating_extractor: RatingExtractor
    ) -> None:
        self.__movie_id_generator = movie_id_generator
        self.__movie_persister = movie_persister
        self.__director_extractor = director_extractor
        self.__genre_extractor = genre_extractor
        self.__rating_extractor = rating_extractor

    def execute(self, request: CreateMovieRequest) -> MovieId:
        movie = Movie.create(
            self.__movie_id_generator,
            request.name,
            request.duration
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

        movie.year = request.year
        movie.poster = request.poster
        movie.poster = request.poster
        movie.trailer = request.trailer

        self.__movie_persister.save(movie)

        return movie.id
