using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public interface IScheduleRepository : IRepository<Schedule, ScheduleId>
    {
    }
}