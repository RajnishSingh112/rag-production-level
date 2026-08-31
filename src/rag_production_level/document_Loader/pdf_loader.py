from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from .base_loader import BaseDocumentLoader

class PDFDocumentLoader(BaseDocumentLoader):
    def load(self, file_path: Path) -> list[Document]:
        loader = PyPDFLoader(str(file_path))
        documents = loader.load()
        return documents