using Showtimes.Scheduler.Domain.Model.Movie;

namespace Showtimes.Scheduler.Application.Movie
{
    public class MovieApplicationService
    {
        private readonly IMovieRepository _moveRepository;

        public MovieApplicationService(IMovieRepository moveRepository)
        {
            _moveRepository = moveRepository;
        }

        public string CreateMovie(CreateMovieCommand command)
        {
            var movie = new Domain.Model.Movie.Movie(
                _moveRepository.GetNextIdentity(),
                command.Name,
                command.Description,
                command.Duration);

            _moveRepository.Save(movie);

            return movie.MovieId.Id;
        }
    }
}