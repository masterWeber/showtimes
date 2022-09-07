using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule.Weekday
{
    public class ListWeekdayRule : ValueObject, IWeekdayRule
    {
        private readonly DayOfWeek[] _days;

        public ListWeekdayRule(DayOfWeek[] days)
        {
            _days = days;
        }

        public bool Match(DateOnly date)
        {
            return Array.Exists(_days, element => element == date.DayOfWeek);
        }

        public override string ToString()
        {
            return string.Join(",", _days);
        }
        
        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return typeof(ListWeekdayRule);
            yield return _days;
        }
    }
}