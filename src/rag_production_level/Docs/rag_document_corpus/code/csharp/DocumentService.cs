using System;
using System.Threading;
using System.Threading.Tasks;

namespace Nexus.Documents;

public sealed class DocumentService
{
    private readonly IDocumentRepository _repository;

    public DocumentService(IDocumentRepository repository)
    {
        _repository = repository;
    }

    public async Task<Document> CreateAsync(
        Document document,
        CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(document.Title))
            throw new ArgumentException("Title is required.");

        var existing = await _repository.FindByHashAsync(
            document.TenantId,
            document.ContentHash,
            cancellationToken);

        if (existing is not null)
            return existing;

        return await _repository.InsertAsync(document, cancellationToken);
    }
}

public interface IDocumentRepository
{
    Task<Document?> FindByHashAsync(string tenantId, string hash, CancellationToken ct);
    Task<Document> InsertAsync(Document document, CancellationToken ct);
}

public sealed record Document(
    string Id,
    string TenantId,
    string Title,
    string ContentHash);
