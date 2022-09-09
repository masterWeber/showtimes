using Showtimes.Scheduler.Domain.Model.Movie;

namespace Showtimes.Scheduler.Infrastructure.Persistence.EFCore
{
    using Microsoft.EntityFrameworkCore;

    public class SchedulerDbContext : DbContext
    {
        public DbSet<Movie> Movies { get; set; }

        public string DbPath { get; }

        public SchedulerDbContext()
        {
            var folder = Environment.SpecialFolder.LocalApplicationData;
            var path = Environment.GetFolderPath(folder);
            DbPath = Path.Join(path, "showtimes.scheduler.db");
        }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
            => options.UseSqlite($"Data Source={DbPath}");

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder
                .Entity<Movie>(m =>
                {
                    m.Property(e => e.MovieId)
                        .HasColumnName("movie_id")
                        .HasColumnType("char(36)")
                        .HasConversion(
                            v => v.ToString(),
                            v => new MovieId(v));

                    m.Property(e => e.Name)
                        .HasColumnName("name")
                        .HasColumnType("varchar(200)");

                    m.Property(e => e.Description)
                        .HasColumnName("description")
                        .HasColumnType("varchar");

                    m.Property(e => e.Duration)
                        .HasColumnName("duration")
                        .HasColumnType("smallint")
                        .HasConversion<int>();
                })
                .Entity<Movie>()
                .ToTable("movie")
                .HasIndex(m => m.MovieId)
                .IsUnique();
        }
    }
}