from abc import ABC, abstractmethod
from pathlib import Path
from langchain_core.documents import Document

class BaseDocumentLoader(ABC):
    @abstractmethod
    def load(self, file_path: Path) -> list[Document]:
        pass