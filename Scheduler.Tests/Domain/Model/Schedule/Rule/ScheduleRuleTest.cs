using Showtimes.Scheduler.Domain.Model.Schedule.MovieSession;
using Showtimes.Scheduler.Domain.Model.Schedule.Rule;
using Showtimes.Scheduler.Domain.Model.Schedule.Rule.DayOfMonth;
using Showtimes.Scheduler.Domain.Model.Schedule.Rule.Weekday;

namespace Showtimes.Scheduler.Tests.Domain.Model.Schedule.Rule
{
    public class ScheduleRuleTest
    {
        [TestCaseSource(nameof(ValidData))]
        public void ToString_ShouldReturnValidExpression(
            HashSet<TimePeriod> timePeriods,
            IDayOfMonthRule dayOfMonth,
            IWeekdayRule weekday,
            string expression)
        {
            var rule = new ScheduleRule(
                timePeriods,
                dayOfMonth,
                weekday);

            Assert.That(expression, Is.EqualTo(rule.ToString()));
        }

        [TestCaseSource(nameof(ValidData))]
        public void FromExpression_ShouldCreateInstance(
            HashSet<TimePeriod> timePeriods,
            IDayOfMonthRule dayOfMonth,
            IWeekdayRule weekday,
            string expression)
        {
            var rule = ScheduleRule.FromExpression(expression);

            Assert.Multiple(() =>
            {
                Assert.That(weekday.ToString(), Is.EqualTo(rule.Weekday.ToString()));
                Assert.That(dayOfMonth.ToString(), Is.EqualTo(rule.DayOfMonth.ToString()));
                Assert.That(timePeriods, Is.EquivalentTo(rule.TimePeriods()));
            });
        }

        private static IEnumerable<object> ValidData()
        {
            var timePeriod = new TimePeriod(
                new TimeOnly(14, 10),
                new TimeOnly(16, 30));

            yield return new object[]
            {
                new HashSet<TimePeriod> { timePeriod },
                new AnyDayOfMonthRule(),
                new AnyWeekdayRule(),
                "14:10-16:30 * *"
            };

            var otherTimePeriod = new TimePeriod(
                new TimeOnly(19, 10),
                new TimeOnly(21, 30));

            yield return new object[]
            {
                new HashSet<TimePeriod> { timePeriod, otherTimePeriod },
                new ListDayOfMonthRule(new[] { 1, 2, 3 }),
                new ListWeekdayRule(new[] { DayOfWeek.Saturday, DayOfWeek.Sunday }),
                "14:10-16:30,19:10-21:30 1,2,3 Saturday,Sunday"
            };

            yield return new object[]
            {
                new HashSet<TimePeriod> { otherTimePeriod, timePeriod },
                new RangeDayOfMonthRule(1, 6),
                new RangeWeekdayRule(DayOfWeek.Monday, DayOfWeek.Tuesday),
                "19:10-21:30,14:10-16:30 1-6 Monday-Tuesday"
            };
        }
    }
}