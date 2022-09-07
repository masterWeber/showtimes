using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Schedule.MovieSession
{
    public class MovieSessionId : Identity
    {
        public MovieSessionId()
        {
        }

        public MovieSessionId(string id) : base(id)
        {
        }
    }
}