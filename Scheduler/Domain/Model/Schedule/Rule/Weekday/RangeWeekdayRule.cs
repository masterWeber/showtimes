using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule.Weekday
{
    public class RangeWeekdayRule : ValueObject, IWeekdayRule
    {
        private readonly DayOfWeek _startDay;
        private readonly DayOfWeek _endDay;

        public RangeWeekdayRule(DayOfWeek startDay, DayOfWeek endDay)
        {
            _startDay = startDay;
            _endDay = endDay;
        }

        public bool Match(DateOnly date)
        {
            return (int)_startDay <= (int)date.DayOfWeek && (int)date.DayOfWeek <= (int)_endDay;
        }

        public override string ToString()
        {
            return $"{_startDay}-{_endDay}";
        }

        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return typeof(RangeWeekdayRule);
            yield return _startDay;
            yield return _endDay;
        }
    }
}