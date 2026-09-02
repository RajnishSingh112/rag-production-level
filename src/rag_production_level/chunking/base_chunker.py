from abc import ABC, abstractmethod
from langchain_core.documents import Document
from pathlib import Path
class BaseChunker(ABC):
    """Interface for text chunkers."""

    @abstractmethod
    def chunk(self, documents: list[Document]) -> list[Document]:
        """Split *text* into chunks."""
        pass

    def add_chunk_metadata(self, chunks: list[Document]) -> list[Document]:
        """Add metadata to each chunk."""
        for index, chunk in enumerate(chunks):
            source = chunk.metadata.get("source", "unknown")
            document_name = Path(source).name
            chunk.metadata["document_id"] = document_name
            chunk.metadata["chunk_index"] = index
            chunk.metadata["chunk_id"] = (
                f"{document_name}_chunk_{index}"
            )
        return chunks
