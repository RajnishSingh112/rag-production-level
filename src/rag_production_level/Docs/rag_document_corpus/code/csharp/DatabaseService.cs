using Npgsql;
using System.Threading;
using System.Threading.Tasks;

namespace Nexus.Infrastructure;

public sealed class DatabaseService
{
    private readonly NpgsqlDataSource _dataSource;

    public DatabaseService(NpgsqlDataSource dataSource)
    {
        _dataSource = dataSource;
    }

    public async Task<int> ExecuteAsync(
        string sql,
        CancellationToken cancellationToken)
    {
        await using var connection =
            await _dataSource.OpenConnectionAsync(cancellationToken);

        await using var command = new NpgsqlCommand(sql, connection);
        return await command.ExecuteNonQueryAsync(cancellationToken);
    }
}
