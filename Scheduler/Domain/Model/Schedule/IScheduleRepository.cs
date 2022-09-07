namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public interface IScheduleRepository
    {
        Schedule Get(ScheduleId scheduleId);
        ScheduleId GetNextIdentity();
        void Save(Schedule schedule);
    }
}