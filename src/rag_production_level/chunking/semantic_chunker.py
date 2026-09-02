from langchain_core.documents import Document
import nltk
from .base_chunker import BaseChunker

class SemanticChunker(BaseChunker):
    def __init__(self):
        # Initialize any necessary components for semantic chunking
        pass

    def split_sentences(self, document: Document) -> list[str]:
        # Implement a method to split the text into sentences
        # This is a placeholder implementation; you can use NLP libraries like spaCy or NLTK for better results
        text = document.page_content
        sentences = nltk.sent_tokenize(text)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences

    def chunk(self, documents: list[Document]) -> list[Document]:
        chunks = []
        for document in documents:
            sentences = self.split_sentences(document)
            for index, sentence in enumerate(sentences):
                chunk_metadata = {
                    "source": document.metadata.get("source", "unknown"),
                    "chunk_index": index,
                    "chunk_id": f"{document.metadata.get('source', 'unknown')}_chunk_{index}"
                }
                chunk = Document(page_content=sentence, metadata=chunk_metadata)
                chunks.append(chunk)
        return chunks