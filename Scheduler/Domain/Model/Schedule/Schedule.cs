using Showtimes.Common.Domain.Model;
using Showtimes.Scheduler.Domain.Model.Schedule.MovieSession;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public class Schedule : IEntity, IEquatable<Schedule>
    {
        public IIdentity Id => ScheduleId;
        public ScheduleId ScheduleId { get; }
        public string Name { get; private set; }

        public Schedule(ScheduleId scheduleId, string name)
        {
            ScheduleId = scheduleId;
            Name = name;

            DomainEventPublisher.Instance.Publish(
                new ScheduleCreated(ScheduleId)
            );
        }

        public void Rename(string name)
        {
            Name = name;

            DomainEventPublisher.Instance.Publish(
                new ScheduleRenamed(
                    ScheduleId,
                    Name
                )
            );
        }

        public MovieSession.MovieSession ScheduleMovieSession(
            ScheduleIdentityService scheduleIdentityService,
            DateOnly date,
            TimePeriod timePeriod,
            HashSet<Movie.Movie>? movies = null)
        {
            return new MovieSession.MovieSession(
                ScheduleId,
                scheduleIdentityService.GetNextMovieSessionIdentity(),
                date,
                timePeriod,
                movies
            );
        }

        public bool Equals(Schedule? other)
        {
            if (ReferenceEquals(this, other)) return true;
            if (ReferenceEquals(null, other)) return false;

            return ScheduleId.Equals(other.ScheduleId);
        }

        public override bool Equals(object? anotherObject)
        {
            return Equals(anotherObject as Schedule);
        }

        public override int GetHashCode()
        {
            return 19578 * 23
                   + HashCode.Combine(Name);
        }
    }
}