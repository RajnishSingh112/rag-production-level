# Metadata Service

The Metadata Service consumes `MetadataRequested` messages.

## Processing sequence

1. Validate message envelope.
2. Load document information.
3. Normalize metadata.
4. Extract metadata using a format-specific parser.
5. Validate required fields.
6. Enrich metadata.
7. Persist using optimistic concurrency.
8. Publish `MetadataCompleted`.

## Failure classification

Transient database/storage failures are retryable. Unsupported formats and malformed
documents are routed to quarantine. After five failed attempts, retryable messages enter
the dead-letter queue.

## Idempotency

The content hash is used to detect duplicate submissions. Processing the same content hash
for the same tenant must not create duplicate published metadata.

See `metadata_rules.txt` and `metadata_generator.cs`.
