using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public interface IMovieRepository : IRepository<Movie, MovieId>
    {
    }
}