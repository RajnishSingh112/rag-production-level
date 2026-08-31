-- Find failed jobs that may need operator review
SELECT id, document_id, attempt_count, failure_reason
FROM processing_jobs
WHERE status = 'Failed'
ORDER BY created_at DESC
LIMIT 50;

-- Check metadata versions for a document
SELECT document_id, metadata_key, version, updated_at
FROM document_metadata
WHERE document_id = :document_id
ORDER BY metadata_key;

-- Find high-volume tenants
SELECT tenant_id, COUNT(*) AS document_count
FROM documents
GROUP BY tenant_id
ORDER BY document_count DESC;
