namespace Showtimes.Common.Domain.Model
{
    class DomainEventSubscriber<TEvent> : IDomainEventSubscriber<TEvent> where TEvent : IDomainEvent
    {
        public DomainEventSubscriber(Action<TEvent> handle)
        {
            _handle = handle;
        }

        readonly Action<TEvent> _handle;

        public void HandleEvent(TEvent domainEvent)
        {
            _handle(domainEvent);
        }

        public Type SubscribedToEventType()
        {
            return typeof(TEvent);
        }
    }
}