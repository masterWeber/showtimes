using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public class MovieScheduled : IDomainEvent
    {
        public int EventVersion { get; set; }
        public DateTime OccurredOn { get; set; }
        public MovieId MovieId { get; }

        public MovieScheduled(
            MovieId movieId)
        {
            MovieId = movieId;
            EventVersion = 1;
            OccurredOn = DateTime.Now;
        }
    }
}