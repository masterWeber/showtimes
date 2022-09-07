using System.Text.RegularExpressions;
using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.MovieSession
{
    public class TimePeriod : ValueObject
    {
        public TimeOnly Start { get; }
        public TimeOnly End { get; }

        public TimePeriod(TimeOnly start, TimeOnly end)
        {
            if (start > end)
            {
                throw new InvalidOperationException("The start cannot come before the end.");
            }

            Start = start;
            End = end;
        }

        public static TimePeriod FromExpression(string expression)
        {
            var pattern = @"(\d{2}):(\d{2})-(\d{2}):(\d{2})";

            Match regexMatch = Regex.Match(expression, pattern);

            if (regexMatch.Success)
            {
                var start = new TimeOnly(
                    Int32.Parse(regexMatch.Groups[1].Value),
                    Int32.Parse(regexMatch.Groups[2].Value));

                var end = new TimeOnly(
                    Int32.Parse(regexMatch.Groups[3].Value),
                    Int32.Parse(regexMatch.Groups[4].Value));

                return new TimePeriod(start, end);
            }

            throw new InvalidOperationException($"Invalid expression '{expression}'");
        }

        public int Duration()
        {
            int endMinutes = End.Hour * 60 + End.Minute;
            int startMinutes = Start.Hour * 60 + Start.Minute;

            return endMinutes - startMinutes;
        }

        protected override IEnumerable<object> GetEqualityComponents()
        {
            yield return Start;
            yield return End;
        }

        public override string ToString()
        {
            return $"{Start.ToString("H:mm")}-{End.ToString("H:mm")}";
        }
    }
}