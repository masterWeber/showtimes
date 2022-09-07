using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.MovieSession
{
    public class MovieSession : Entity, IEquatable<MovieSession>
    {
        public ScheduleId ScheduleId { get; }
        public MovieSessionId MovieSessionId { get; }
        public DateOnly Date { get; }
        public TimePeriod TimePeriod { get; }
        public HashSet<Movie.Movie> Movies { get; }

        public MovieSession(
            ScheduleId scheduleId,
            MovieSessionId movieSessionId,
            DateOnly date,
            TimePeriod timePeriod,
            IEnumerable<Movie.Movie>? movies = null)
        {
            ScheduleId = scheduleId;
            MovieSessionId = movieSessionId;
            Date = date;
            TimePeriod = timePeriod;
            Movies = new HashSet<Movie.Movie>(
                movies ?? Enumerable.Empty<Movie.Movie>()
            );
        }

        public bool MovieSelected()
        {
            return Movies.Any();
        }

        public void AddMovie(Movie.Movie movie)
        {
            if (FreeTime() < movie.Duration)
            {
                throw new InvalidOperationException("The movie is too long.");
            }

            Movies.Add(movie);
        }

        public int FreeTime()
        {
            var timePeriodDuration = TimePeriod.Duration();
            var moviesTotalDuration = Movies.Sum(movie => movie.Duration);

            return timePeriodDuration - moviesTotalDuration;
        }

        public bool Equals(MovieSession? other)
        {
            if (ReferenceEquals(this, other)) return true;
            if (ReferenceEquals(null, other)) return false;

            return MovieSessionId.Equals(other.MovieSessionId);
        }

        public override bool Equals(object? anotherObject)
        {
            return Equals(anotherObject as MovieSession);
        }

        public override int GetHashCode()
        {
            return 73281 * 47
                   + HashCode.Combine(Date, TimePeriod, Movies);
        }
    }
}