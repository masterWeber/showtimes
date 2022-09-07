using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule.DayOfMonth;

public class AnyDayOfMonthRule : ValueObject, IDayOfMonthRule
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
        yield return typeof(AnyDayOfMonthRule);
    }
}