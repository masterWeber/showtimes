namespace Showtimes.Scheduler.Domain.Model.Schedule.MovieSession
{
    public interface IMovieSessionRepository
    {
        MovieSession Get(MovieSessionId movieSessionId);
        MovieSessionId GetNextIdentity();
        void Save(MovieSession movieSession);
    }
}