package com.nexus.processing;

public final class DocumentProcessingService {
    public ProcessingResult process(Document document) {
        if (document.contentHash() == null) {
            throw new IllegalArgumentException("content hash required");
        }

        // Binary content is stored in object storage.
        // Metadata and processing state are stored in PostgreSQL.
        return ProcessingResult.queued(document.id());
    }
}
