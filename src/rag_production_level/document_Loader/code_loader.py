from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from .base_loader import BaseDocumentLoader


class CodeDocumentLoader(BaseDocumentLoader):

    def load(self, file_path: Path) -> list[Document]:

        loader = TextLoader(
            str(file_path),
            encoding="utf-8"
        )

        documents = loader.load()

        for document in documents:
            document.metadata["file_type"] = "code"
            document.metadata["language"] = self._get_language(file_path)

        return documents

    def _get_language(self, file_path: Path) -> str:

        extension = file_path.suffix.lower()

        languages = {
            ".cs": "csharp",
            ".java": "java",
            ".py": "python",
            ".sql": "sql"
        }

        return languages.get(extension, "unknown")