CREATE TABLE documents (
    id UUID PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL,
    title TEXT NOT NULL,
    content_hash VARCHAR(128) NOT NULL,
    classification VARCHAR(32) NOT NULL,
    status VARCHAR(32) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX ux_documents_tenant_hash
    ON documents (tenant_id, content_hash);

CREATE INDEX ix_documents_tenant_status
    ON documents (tenant_id, status);

CREATE TABLE document_metadata (
    id BIGSERIAL PRIMARY KEY,
    document_id UUID NOT NULL REFERENCES documents(id),
    metadata_key VARCHAR(128) NOT NULL,
    metadata_value TEXT,
    version BIGINT NOT NULL DEFAULT 1,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ix_document_metadata_document
    ON document_metadata (document_id);

CREATE TABLE processing_jobs (
    id UUID PRIMARY KEY,
    document_id UUID NOT NULL REFERENCES documents(id),
    status VARCHAR(32) NOT NULL,
    attempt_count INT NOT NULL DEFAULT 0,
    failure_reason TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
