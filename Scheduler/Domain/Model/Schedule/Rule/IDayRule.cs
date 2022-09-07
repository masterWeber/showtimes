using System.Runtime.Serialization;

namespace Showtimes.Scheduler.Domain.Model.Schedule.Rule
{
    public interface IDayRule
    {
        public bool Match(DateOnly date);
    }
}