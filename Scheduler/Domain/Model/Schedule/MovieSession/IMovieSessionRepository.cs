using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.MovieSession
{
    public interface IMovieSessionRepository : IRepository<MovieSession, MovieSessionId>
    {
    }
}