using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public class ScheduleId : Identity
    {
        public ScheduleId()
        {
        }

        public ScheduleId(string id) : base(id)
        {
        }
    }
}