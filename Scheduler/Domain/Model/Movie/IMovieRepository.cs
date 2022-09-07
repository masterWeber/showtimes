namespace Showtimes.Scheduler.Domain.Model.Movie
{
    public interface IMovieRepository
    {
        MovieId GetNextIdentity();

        Movie Get(MovieId movieId);

        void Remove(Movie movie);

        void RemoveAll(IEnumerable<Movie> movies);

        void Save(Movie movie);

        void SaveAll(IEnumerable<Movie> movies);
    }
}