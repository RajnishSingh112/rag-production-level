# Data Flow

```text
WPF Client
   |
   v
API Gateway ---> PostgreSQL (metadata/state)
   |
   v
Document Processing Service ---> Object Storage
   |
   v
Message Broker
   |
   v
Metadata Service ---> PostgreSQL
   |
   v
Audit / Events
```

Binary document content is stored in object storage. Searchable metadata and processing
state are stored in PostgreSQL.

The desktop client never connects directly to PostgreSQL.
