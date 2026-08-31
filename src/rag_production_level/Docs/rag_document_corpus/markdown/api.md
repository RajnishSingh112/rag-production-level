# API Integration Guide

## Create a document

`POST /api/v1/documents`

The request includes tenant information, file metadata, and the document payload.

The response contains a `document_id` and an asynchronous `processing_job_id`.

## Reprocess

`POST /api/v1/documents/{id}/reprocess`

This endpoint requires the Operator role.

## Pagination

Use `page` and `page_size`. Default is 50, maximum is 200.

## Concurrency

Metadata updates include a version. If the version is stale, the server returns 409.
Clients should fetch the current resource before retrying.
