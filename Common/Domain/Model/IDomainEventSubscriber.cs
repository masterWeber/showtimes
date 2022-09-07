namespace Showtimes.Common.Domain.Model
{
    public interface IDomainEventSubscriber<in T> where T : IDomainEvent
    {
        void HandleEvent(T domainEvent);
        Type SubscribedToEventType();
    }
}