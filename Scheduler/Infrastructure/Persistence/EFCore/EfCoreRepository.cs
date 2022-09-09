using Microsoft.EntityFrameworkCore;
using Showtimes.Common.Domain.Model;

namespace Showtimes.Scheduler.Infrastructure.Persistence.EFCore
{
    public abstract class EfCoreRepository<TEntity, TIdentity, TContext> : IRepository<TEntity, TIdentity>
        where TEntity : class, IEntity
        where TIdentity : class, IIdentity, new()
        where TContext : DbContext
    {
        private readonly TContext _context;

        public EfCoreRepository(TContext context)
        {
            _context = context;
        }

        public TIdentity GetNextIdentity()
        {
            return new TIdentity();
        }

        public async void Save(TEntity entity)
        {
            var existsEntity = await _context.Set<TEntity>().FindAsync(entity.Id.Id);

            if (existsEntity == null)
            {
                _context.Set<TEntity>().Add(entity);
            }
            else
            {
                _context.Entry(entity).State = EntityState.Modified;
            }

            await _context.SaveChangesAsync();
        }

        public void SaveAll(IEnumerable<TEntity> entities)
        {
            foreach (var entity in entities)
            {
                Save(entity);
            }
        }

        public async void Remove(TEntity entity)
        {
            var existsEntity = await _context.Set<TEntity>().FindAsync(entity.Id.Id);
            if (existsEntity == null)
            {
                return;
            }

            _context.Set<TEntity>().Remove(entity);
            await _context.SaveChangesAsync();
        }

        public void RemoveAll(IEnumerable<TEntity> entities)
        {
            foreach (var entity in entities)
            {
                Remove(entity);
            }
        }

        public async Task<TEntity?> Get(TIdentity id)
        {
            return await _context.Set<TEntity>().FindAsync(id.Id);
        }
    }
}