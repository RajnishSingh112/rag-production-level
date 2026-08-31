# Deployment Guide

The platform is containerized.

Required services:
- API Gateway
- Document Processing Service
- Metadata Service
- PostgreSQL
- Object Storage
- Message Broker

Readiness checks must validate required dependencies. Liveness checks should not perform
expensive external operations.

Metadata Service should scale with queue depth. API Gateway should scale with request rate.

Configuration is supplied through environment variables or mounted configuration files.
Secrets must not be committed to source control.
