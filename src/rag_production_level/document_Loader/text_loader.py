from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from .base_loader import BaseDocumentLoader

class TextDocumentLoader(BaseDocumentLoader):
    def load(self, file_path: Path) -> list[Document]:
        loader = TextLoader(str(file_path), encoding="utf-8")
        documents = loader.load()
        return documents