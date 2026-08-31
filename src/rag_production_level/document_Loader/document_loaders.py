from pathlib import Path

from langchain_core.documents import Document

from .base_loader import BaseDocumentLoader
from .pdf_loader import PDFDocumentLoader
from .text_loader import TextDocumentLoader
from .code_loader import CodeDocumentLoader


class DocumentLoader:

    def __init__(self):

        self._loaders: dict[str, BaseDocumentLoader] = {
            ".pdf": PDFDocumentLoader(),
            ".txt": TextDocumentLoader(),
            ".md": TextDocumentLoader(),
            ".cs": CodeDocumentLoader(),
            ".java": CodeDocumentLoader(),
            ".py": CodeDocumentLoader(),
            ".sql": CodeDocumentLoader(),
        }

    def load_file(self, file_path: Path) -> list[Document]:

        extension = file_path.suffix.lower()

        loader = self._loaders.get(extension)

        if loader is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader.load(file_path)