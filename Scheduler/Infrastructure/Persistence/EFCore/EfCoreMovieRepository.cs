using Showtimes.Scheduler.Domain.Model.Movie;

namespace Showtimes.Scheduler.Infrastructure.Persistence.EFCore
{
    public class EfCoreMovieRepository : EfCoreRepository<Movie, MovieId, SchedulerDbContext>, IMovieRepository
    {
        public EfCoreMovieRepository(SchedulerDbContext context) : base(context)
        {
        }
    }
}