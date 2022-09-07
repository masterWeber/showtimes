using Showtimes.Scheduler.Domain.Model.Schedule.MovieSession;

namespace Showtimes.Scheduler.Tests.Domain.Model.Schedule.MovieSession
{
    public class TimePeriodTest
    {
        [TestCase(14, 10, 16, 40, ExpectedResult = 150)]
        [TestCase(19, 10, 21, 40, ExpectedResult = 150)]
        [TestCase(10, 00, 21, 40, ExpectedResult = 700)]
        [TestCase(11, 00, 11, 40, ExpectedResult = 40)]
        public int Duration_ShouldReturnDifferenceInMinutes(
            int startHour,
            int startMinute,
            int endHour,
            int endMinute)
        {
            var start = new TimeOnly(startHour, startMinute);
            var end = new TimeOnly(endHour, endMinute);

            var timePeriod = new TimePeriod(start, end);

            return timePeriod.Duration();
        }

        [TestCase(19, 10, 20, 40, ExpectedResult = true)]
        [TestCase(14, 10, 16, 40, ExpectedResult = true)]
        public bool Equals_ShouldReturnTrue(
            int startHour,
            int startMinute,
            int endHour,
            int endMinute)
        {
            var startA = new TimeOnly(startHour, startMinute);
            var endA = new TimeOnly(endHour, endMinute);

            var timePeriodA = new TimePeriod(startA, endA);

            var startB = new TimeOnly(startHour, startMinute);
            var endB = new TimeOnly(endHour, endMinute);

            var timePeriodB = new TimePeriod(startB, endB);

            return timePeriodA.Equals(timePeriodB);
        }

        [Test]
        [ExpectedException(typeof(InvalidOperationException))]
        [TestCase(21, 30, 19, 10)]
        [TestCase(16, 30, 14, 10)]
        public void InvalidOperationException_WhenEndBeforeStart(
            int startHour,
            int startMinute,
            int endHour,
            int endMinute)
        {
            var start = new TimeOnly(startHour, startMinute);
            var end = new TimeOnly(endHour, endMinute);

            var timePeriod = new TimePeriod(start, end);
        }

        [ExpectedException(typeof(InvalidOperationException))]
        [TestCase("")]
        [TestCase("14:1016:30")]
        [TestCase("4:10-16:30")]
        [TestCase("14-16:30")]
        [TestCase("16:30")]
        public void FromString_InvalidOperationException_WhenInvalidExpression(string expression)
        {
            TimePeriod.FromExpression(expression);
        }

        [TestCase("14:10-16:30")]
        [TestCase("19:10-21:30")]
        [TestCase("10:00-12:30")]
        public void FromString_ShouldCreateInstance_WhenValidExpression(string expression)
        {
            var timePeriod = TimePeriod.FromExpression(expression);

            Assert.IsNotNull(timePeriod);
            Assert.IsInstanceOf<TimePeriod>(timePeriod);
        }
    }
}