using Showtimes.Scheduler.Domain.Model.Schedule.MovieSession;
using Showtimes.Scheduler.Domain.Model.Schedule.Rule;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public class ScheduleGenerateService
    {
        private readonly ScheduleIdentityService _scheduleIdentityService;

        public ScheduleGenerateService(ScheduleIdentityService scheduleIdentityService)
        {
            _scheduleIdentityService = scheduleIdentityService;
        }

        public Schedule Generate(
            string name,
            DateOnly startDate,
            DateOnly endDate,
            ScheduleRule scheduleRule)
        {
            var schedule = new Schedule(
                _scheduleIdentityService.GetNextScheduleId(),
                name
            );

            foreach (var day in EachDay(startDate, endDate))
            {
                if (scheduleRule.DayOfMonth.Match(day) && scheduleRule.Weekday.Match(day))
                {
                    foreach (var timePeriod in scheduleRule.TimePeriods())
                    {
                        schedule.ScheduleMovieSession(
                            _scheduleIdentityService,
                            day,
                            timePeriod
                        );
                    }
                }
            }

            return schedule;
        }

        private IEnumerable<DateOnly> EachDay(DateOnly from, DateOnly thru)
        {
            for (var day = from; day <= thru; day = day.AddDays(1))
                yield return day;
        }
    }
}