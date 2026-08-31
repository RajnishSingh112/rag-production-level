using System;
using System.Collections.Generic;

namespace Nexus.Metadata;

public sealed record MetadataInput(
    string DocumentId,
    string ContentType,
    string SourceName,
    string ContentHash);

public sealed record ExtractedMetadata(
    string DocumentId,
    Dictionary<string, string> Values,
    DateTime ExtractedAtUtc);

public interface IMetadataExtractor
{
    bool CanHandle(string contentType);
    ExtractedMetadata Extract(MetadataInput input, string content);
}

public sealed class MetadataGenerator
{
    private readonly IEnumerable<IMetadataExtractor> _extractors;

    public MetadataGenerator(IEnumerable<IMetadataExtractor> extractors)
    {
        _extractors = extractors;
    }

    public ExtractedMetadata Generate(MetadataInput input, string content)
    {
        if (string.IsNullOrWhiteSpace(input.DocumentId))
            throw new ArgumentException("DocumentId is required.");

        foreach (var extractor in _extractors)
        {
            if (extractor.CanHandle(input.ContentType))
                return extractor.Extract(input, content);
        }

        throw new NotSupportedException(
            $"Unsupported content type: {input.ContentType}");
    }
}
