using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public class ScheduleRenamed : IDomainEvent
    {
        public int EventVersion { get; set; }
        public DateTime OccurredOn { get; set; }
        public ScheduleId ScheduleId { get; }
        public string Name { get; }

        public ScheduleRenamed(
            ScheduleId movieId,
            string name)
        {
            ScheduleId = movieId;
            Name = name;
            EventVersion = 1;
            OccurredOn = DateTime.Now;
        }
    }
}