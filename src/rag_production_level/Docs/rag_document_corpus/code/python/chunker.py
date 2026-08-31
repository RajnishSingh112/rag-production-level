from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class DocumentChunk:
    chunk_id: str
    document_id: str
    text: str
    metadata: dict[str, str]


class ChunkingStrategy(Protocol):
    def chunk(self, document_id: str, text: str) -> list[DocumentChunk]: ...


class SimpleChunker:
    def __init__(self, chunk_size: int = 500) -> None:
        self.chunk_size = chunk_size

    def chunk(self, document_id: str, text: str) -> list[DocumentChunk]:
        words = text.split()
        chunks: list[DocumentChunk] = []

        for start in range(0, len(words), self.chunk_size):
            part = " ".join(words[start:start + self.chunk_size])
            chunks.append(
                DocumentChunk(
                    chunk_id=f"{document_id}-{start}",
                    document_id=document_id,
                    text=part,
                    metadata={"strategy": "simple"},
                )
            )

        return chunks
