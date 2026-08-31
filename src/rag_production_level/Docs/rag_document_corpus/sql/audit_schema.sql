CREATE TABLE audit_events (
    id BIGSERIAL PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL,
    request_id UUID NOT NULL,
    event_type VARCHAR(64) NOT NULL,
    actor_id VARCHAR(128),
    document_id UUID,
    event_time TIMESTAMPTZ NOT NULL DEFAULT now(),
    details JSONB
);

CREATE INDEX ix_audit_events_tenant_time
    ON audit_events (tenant_id, event_time);

CREATE INDEX ix_audit_events_request
    ON audit_events (request_id);
