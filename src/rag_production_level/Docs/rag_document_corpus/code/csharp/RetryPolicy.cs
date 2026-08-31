using System;

namespace Nexus.Processing;

public static class RetryPolicy
{
    public const int MaxAttempts = 5;
    public const int InitialDelaySeconds = 2;
    public const int MaxDelaySeconds = 60;

    public static TimeSpan GetDelay(int attempt)
    {
        var seconds = InitialDelaySeconds * Math.Pow(2, attempt - 1);
        return TimeSpan.FromSeconds(Math.Min(seconds, MaxDelaySeconds));
    }

    public static bool IsRetryable(Exception ex)
    {
        return ex is TimeoutException ||
               ex is NpgsqlException;
    }
}
