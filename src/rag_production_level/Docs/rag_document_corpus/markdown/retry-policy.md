# Retry Policy

The processing system uses exponential backoff.

Default:
- Maximum attempts: 5
- Initial delay: 2 seconds
- Backoff multiplier: 2
- Maximum delay: 60 seconds

Retryable examples:
- temporary database unavailable
- object storage timeout
- OCR model temporarily unavailable

Non-retryable examples:
- unsupported file format
- malformed document
- missing required document identifier

After the fifth failed attempt, the message is moved to the dead-letter queue.

Operators should inspect the failure reason before replaying a dead-letter message.
