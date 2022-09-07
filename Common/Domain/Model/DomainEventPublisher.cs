namespace Showtimes.Common.Domain.Model
{
    public class DomainEventPublisher
    {
        [ThreadStatic] private static DomainEventPublisher? _instance;

        public static DomainEventPublisher Instance
        {
            get { return _instance ??= new DomainEventPublisher(); }
        }

        private DomainEventPublisher()
        {
            _publishing = false;
            _subscribers = new List<IDomainEventSubscriber<IDomainEvent>>();
        }

        private bool _publishing;

        private readonly List<IDomainEventSubscriber<IDomainEvent>> _subscribers;

        public void Publish<T>(T domainEvent) where T : IDomainEvent
        {
            if (!_publishing && HasSubscribers())
            {
                try
                {
                    _publishing = true;

                    var eventType = domainEvent.GetType();

                    foreach (var subscriber in _subscribers)
                    {
                        var subscribedToType = subscriber.SubscribedToEventType();
                        if (eventType == subscribedToType || subscribedToType == typeof(IDomainEvent))
                        {
                            subscriber.HandleEvent(domainEvent);
                        }
                    }
                }
                finally
                {
                    _publishing = false;
                }
            }
        }

        public void PublishAll(ICollection<IDomainEvent> domainEvents)
        {
            foreach (var domainEvent in domainEvents)
            {
                Publish(domainEvent);
            }
        }

        public void Reset()
        {
            if (!_publishing)
            {
                _subscribers.Clear();
            }
        }

        public void Subscribe(IDomainEventSubscriber<IDomainEvent> subscriber)
        {
            if (!_publishing)
            {
                _subscribers.Add(subscriber);
            }
        }

        public void Subscribe(Action<IDomainEvent> handle)
        {
            Subscribe(new DomainEventSubscriber<IDomainEvent>(handle));
        }

        bool HasSubscribers()
        {
            return _subscribers.Count != 0;
        }
    }
}