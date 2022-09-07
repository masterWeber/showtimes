using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public class MovieDescriptionChanged : IDomainEvent
    {
        public int EventVersion { get; set; }
        public DateTime OccurredOn { get; set; }
        public MovieId MovieId { get; }
        public string Description { get; }

        public MovieDescriptionChanged(
            MovieId movieId,
            string description)
        {
            MovieId = movieId;
            Description = description;
            EventVersion = 1;
            OccurredOn = DateTime.Now;
        }
    }
}