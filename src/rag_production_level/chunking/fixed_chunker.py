from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document
from .base_chunker import BaseChunker

class FixedChunker(BaseChunker):
    def __init__(self, chunk_size:int=500, chunk_overlap:int=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)

    def chunk(self, documents: list[Document]) -> list[Document]:
        chunks = self.text_splitter.split_documents(documents)
        return self.add_chunk_metadata(chunks)