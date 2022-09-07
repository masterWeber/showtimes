using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public class ScheduleCreated : IDomainEvent
    {
        public int EventVersion { get; set; }
        public DateTime OccurredOn { get; set; }
        public ScheduleId ScheduleId { get; }

        public ScheduleCreated(
            ScheduleId scheduleId)
        {
            ScheduleId = scheduleId;
            EventVersion = 1;
            OccurredOn = DateTime.Now;
        }
    }
}