using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public class MovieId : Identity
    {
        public MovieId()
        {
        }

        public MovieId(string id) : base(id)
        {
        }
    }
}