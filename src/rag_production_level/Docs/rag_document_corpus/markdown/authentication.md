# Authentication and Authorization

## OAuth

The API Gateway validates OAuth 2.0 bearer access tokens. Access tokens are not passed
through to PostgreSQL or stored in the application database.

## Roles

- Viewer: read documents permitted by tenant and classification.
- Contributor: create and update documents.
- Operator: reprocess documents and replay selected failed jobs.
- Administrator: manage users and system configuration.

## Service-to-Service Authentication

Internal services use short-lived service credentials injected through environment
variables. See `application.json`.

## Token Failures

Invalid or expired tokens produce HTTP 401. A valid token without the required role
produces HTTP 403.

For security requirements, see `security_architecture.pdf`.
