using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public class Movie : Entity, IEquatable<Movie>
    {
        public MovieId MovieId { get; }
        public string Name { get; private set; }
        public string Description { get; private set; }
        public int Duration { get; }

        public Movie(
            MovieId movieId,
            string name,
            string description,
            int duration)
        {
            MovieId = movieId;
            Name = name;
            Description = description;
            Duration = duration;

            DomainEventPublisher.Instance.Publish(
                new MovieCreated(MovieId)
            );
        }

        public void Rename(string name)
        {
            Name = name;

            DomainEventPublisher.Instance.Publish(
                new MovieRenamed(
                    MovieId,
                    Name
                )
            );
        }

        public void ChangeDescription(string description)
        {
            Description = description;

            DomainEventPublisher.Instance.Publish(
                new MovieDescriptionChanged(
                    MovieId,
                    Description
                )
            );
        }

        public bool Equals(Movie? other)
        {
            if (ReferenceEquals(this, other)) return true;
            if (ReferenceEquals(null, other)) return false;

            return MovieId.Equals(other.MovieId);
        }

        public override bool Equals(object? anotherObject)
        {
            return Equals(anotherObject as Movie);
        }

        public override int GetHashCode()
        {
            return 2335 * 3 + HashCode.Combine(Name, Description, Duration);
        }
    }
}