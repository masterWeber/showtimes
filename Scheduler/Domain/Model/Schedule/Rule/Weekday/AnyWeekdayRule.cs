using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule.Weekday
{
    public class AnyWeekdayRule : ValueObject, IWeekdayRule
    {
        public bool Match(DateOnly date)
        {
            return true;
        }

        public override string ToString()
        {
            return "*";
        }

        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return typeof(AnyWeekdayRule);
        }
    }
}