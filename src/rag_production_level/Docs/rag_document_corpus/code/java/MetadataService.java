package com.nexus.metadata;

public final class MetadataService {
    private final MetadataRepository repository;
    private final MetadataExtractor extractor;

    public MetadataService(MetadataRepository repository,
                           MetadataExtractor extractor) {
        this.repository = repository;
        this.extractor = extractor;
    }

    public MetadataResult process(MetadataRequest request) {
        validate(request);

        MetadataResult result = extractor.extract(
            request.documentId(),
            request.contentType(),
            request.content()
        );

        repository.saveWithVersionCheck(result, request.expectedVersion());
        return result;
    }

    private void validate(MetadataRequest request) {
        if (request.documentId() == null || request.documentId().isBlank()) {
            throw new IllegalArgumentException("documentId is required");
        }
    }
}
