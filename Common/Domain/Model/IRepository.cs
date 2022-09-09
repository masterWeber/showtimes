namespace Showtimes.Common.Domain.Model;

public interface IRepository<TEntity, TIdentity>
    where TEntity : class, IEntity
    where TIdentity : class, IIdentity
{
    TIdentity GetNextIdentity();

    Task<TEntity?> Get(TIdentity id);

    void Remove(TEntity entity);

    void RemoveAll(IEnumerable<TEntity> entities);

    void Save(TEntity entity);

    void SaveAll(IEnumerable<TEntity> entities);
}