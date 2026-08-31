from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Document:
    document_id: str
    tenant_id: str
    title: str
    content_hash: str


class DocumentRepository(Protocol):
    def find_by_hash(self, tenant_id: str, content_hash: str) -> Document | None: ...
    def insert(self, document: Document) -> Document: ...


class DocumentService:
    def __init__(self, repository: DocumentRepository) -> None:
        self.repository = repository

    def create(self, document: Document) -> Document:
        if not document.title.strip():
            raise ValueError("title is required")

        existing = self.repository.find_by_hash(
            document.tenant_id, document.content_hash
        )
        if existing:
            return existing

        return self.repository.insert(document)
