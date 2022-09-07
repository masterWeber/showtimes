using Showtimes.Common.Domain.Model;
using Showtimes.Scheduler.Domain.Model.Schedule.MovieSession;
using Showtimes.Scheduler.Domain.Model.Schedule.Rule.DayOfMonth;
using Showtimes.Scheduler.Domain.Model.Schedule.Rule.Weekday;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule
{
    public class ScheduleRule : ValueObject
    {
        private readonly HashSet<TimePeriod> _timePeriods;
        public IDayOfMonthRule DayOfMonth { get; }
        public IWeekdayRule Weekday { get; }

        public ScheduleRule(
            HashSet<TimePeriod> timePeriods,
            IDayOfMonthRule dayOfMonth,
            IWeekdayRule weekday)
        {
            if (!timePeriods.Any())
            {
                throw new InvalidOperationException("The start cannot come before the end.");
            }

            DayOfMonth = dayOfMonth;
            Weekday = weekday;
            _timePeriods = timePeriods;
        }

        public HashSet<TimePeriod> TimePeriods()
        {
            return _timePeriods.ToHashSet();
        }

        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return TimePeriods();
            yield return DayOfMonth;
            yield return Weekday;
        }

        public static ScheduleRule FromExpression(string expression)
        {
            var parts = expression.Split(" ");
            if (parts.Length != 3)
            {
                throw new InvalidOperationException($"Invalid expression '{expression}'");
            }

            var timePeriods = new HashSet<TimePeriod>();
            foreach (var timePeriodExpression in parts[0].Split(","))
            {
                timePeriods.Add(TimePeriod.FromExpression(timePeriodExpression));
            }

            var dayOfMonthRule = DayOfMonthRuleFromExpression(parts[1]);
            var weekdayRule = WeekdayRuleFromExpression(parts[2]);

            return new ScheduleRule(timePeriods, dayOfMonthRule, weekdayRule);
        }

        private static IDayOfMonthRule DayOfMonthRuleFromExpression(string expression)
        {
            if (expression.Equals("*"))
            {
                return new AnyDayOfMonthRule();
            }

            if (expression.Contains(','))
            {
                var dayList = Array.ConvertAll(expression.Split(','), int.Parse);
                return new ListDayOfMonthRule(dayList);
            }

            if (expression.Contains('-'))
            {
                var dayRange = Array.ConvertAll(expression.Split('-'), int.Parse);
                return new RangeDayOfMonthRule(dayRange[0], dayRange[1]);
            }

            throw new InvalidOperationException($"Invalid expression '{expression}'");
        }

        private static IWeekdayRule WeekdayRuleFromExpression(string expression)
        {
            if (expression.Equals("*"))
            {
                return new AnyWeekdayRule();
            }

            if (expression.Contains(','))
            {
                var dayList = expression.Split(',')
                    .Select(Enum.Parse<DayOfWeek>).ToArray();
                return new ListWeekdayRule(dayList);
            }

            if (expression.Contains('-'))
            {
                var dayRange = expression.Split('-')
                    .Select(Enum.Parse<DayOfWeek>).ToArray();
                return new RangeWeekdayRule(dayRange[0], dayRange[1]);
            }

            throw new InvalidOperationException($"Invalid expression '{expression}'");
        }

        public override string ToString()
        {
            return $"{string.Join(",", _timePeriods)} {DayOfMonth} {Weekday}";
        }
    }
}