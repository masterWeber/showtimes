namespace Showtimes.Common.Domain.Model
{
    internal static class HashCodeHelper
    {
        public static int CombineHashCodes(IEnumerable<object> objs)
        {
            unchecked
            {
                var hash = 17;
                foreach (var obj in objs)
                    hash = hash * 23 + obj.GetHashCode();
                return hash;
            }
        }
    }
}