using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public class MovieRenamed : IDomainEvent
    {
        public int EventVersion { get; set; }
        public DateTime OccurredOn { get; set; }
        public MovieId MovieId { get; }
        public string Name { get; }

        public MovieRenamed(
            MovieId movieId,
            string name)
        {
            MovieId = movieId;
            Name = name;
            EventVersion = 1;
            OccurredOn = DateTime.Now;
        }
    }
}