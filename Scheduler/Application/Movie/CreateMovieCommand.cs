namespace Showtimes.Scheduler.Application.Movie
{
    public class CreateMovieCommand
    {
        public string Name { get; set; }
        public string Description { get; set; }
        public int Duration { get; set; }

        public CreateMovieCommand(string name, string description, int duration)
        {
            Name = name;
            Description = description;
            Duration = duration;
        }
    }
}