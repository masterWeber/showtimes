using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule.DayOfMonth
{
    public class RangeDayOfMonthRule : ValueObject, IDayOfMonthRule
    {
        private readonly int _startDay;
        private readonly int _endDay;

        public RangeDayOfMonthRule(int startDay, int endDay)
        {
            _startDay = startDay;
            _endDay = endDay;
        }

        public bool Match(DateOnly date)
        {
            return _startDay <= date.Day && date.Day <= _endDay;
        }

        public override string ToString()
        {
            return $"{_startDay}-{_endDay}";
        }

        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return typeof(RangeDayOfMonthRule);
            yield return _startDay;
            yield return _endDay;
        }
    }
}