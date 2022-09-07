using Showtimes.Scheduler.Domain.Model.Schedule.MovieSession;

namespace Showtimes.Scheduler.Domain.Model.Schedule
{
    public class ScheduleIdentityService
    {
        private readonly IScheduleRepository _scheduleRepository;
        private readonly IMovieSessionRepository _movieSessionRepository;

        public ScheduleIdentityService(
            IScheduleRepository scheduleRepository,
            IMovieSessionRepository movieSessionRepository)
        {
            _scheduleRepository = scheduleRepository;
            _movieSessionRepository = movieSessionRepository;
        }

        public ScheduleId GetNextScheduleId()
        {
            return _scheduleRepository.GetNextIdentity();
        }

        public MovieSessionId GetNextMovieSessionIdentity()
        {
            return _movieSessionRepository.GetNextIdentity();
        }
    }
}