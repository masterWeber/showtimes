using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule.DayOfMonth
{
    public class ListDayOfMonthRule : ValueObject, IDayOfMonthRule
    {
        private readonly int[] _days;

        public ListDayOfMonthRule(int[] days)
        {
            _days = days;
        }

        public bool Match(DateOnly date)
        {
            return Array.Exists(_days, element => element == date.Day);
        }

        public override string ToString()
        {
            return string.Join(",", _days);
        }

        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return typeof(ListDayOfMonthRule);
            yield return _days;
        }
    }
}