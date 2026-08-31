from dataclasses import dataclass


@dataclass(frozen=True)
class MetadataRecord:
    document_id: str
    content_type: str
    source_name: str
    extracted_at_utc: str


class MetadataPipeline:
    def normalize(self, record: MetadataRecord) -> MetadataRecord:
        return MetadataRecord(
            document_id=record.document_id.strip(),
            content_type=record.content_type.lower().strip(),
            source_name=record.source_name.strip(),
            extracted_at_utc=record.extracted_at_utc,
        )

    def validate(self, record: MetadataRecord) -> None:
        required = {
            "document_id": record.document_id,
            "content_type": record.content_type,
            "source_name": record.source_name,
            "extracted_at_utc": record.extracted_at_utc,
        }

        missing = [name for name, value in required.items() if not value]
        if missing:
            raise ValueError(f"Missing metadata: {', '.join(missing)}")
