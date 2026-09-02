from langchain_core.documents import Document
import nltk
import numpy as np
from rag_production_level.embeddings.base_embedding import BaseEmbedding
from .base_chunker import BaseChunker

class SemanticChunker(BaseChunker):
    def __init__(self, embedding_model:BaseEmbedding):
        # Initialize any necessary components for semantic chunking
        self.embedding_model = embedding_model

    def split_sentences(self, document: Document) -> list[str]:
        # Implement a method to split the text into sentences
        text = document.page_content
        sentences = nltk.sent_tokenize(text)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences

    def embed_sentences(self, sentences: list[str]) -> list[list[float]]:
        # Use the embedding model to get embeddings for each sentence
        embeddings = [self.embedding_model.embed_text(sentence) for sentence in sentences]
        return embeddings
    
    def calculate_similarity(self, vector_a: list[float], vector_b: list[float]) -> float:
        # Implement a method to calculate similarity between two embeddings
        # For example, you can use cosine similarity
        
        embedding1 = np.array(vector_a)
        embedding2 = np.array(vector_b)
        similarity = np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
        return similarity
    
    def find_boundary(self, similarity:list[float]) -> list[int]:
        threshold = np.percentile(similarity, 20)  # You can adjust the percentile as needed
        boundary_indices = []
        for index, value in enumerate(similarity):
            if value < threshold:
                boundary_indices.append(index)
        return boundary_indices
    
    def chunk(self, documents: list[Document]) -> list[Document]:
        all_chunks = []
        for document in documents:
            sentences = self.split_sentences(document)
            embedded_sentences = self.embed_sentences(sentences)

            similarities = []

            for i in range(len(embedded_sentences) - 1):
                similarity = self.calculate_similarity(embedded_sentences[i], embedded_sentences[i + 1])
                similarities.append(similarity)

            boundary_indices = self.find_boundary(similarities)

            chunks = self.create_chunks(document, sentences, boundary_indices)
            all_chunks.extend(chunks)
        return self.add_chunk_metadata(all_chunks)

    def create_chunks(self, document: Document, sentences: list[str], boundary_indices: list[int]) -> list[Document]:
        chunks = []
        start_index = 0

        for boundary_index in boundary_indices:
            chunk_sentences = sentences[start_index:boundary_index + 1]
            chunk_text = " ".join(chunk_sentences)
            chunk_document = Document(page_content=chunk_text, metadata=document.metadata.copy())
            chunks.append(chunk_document)
            start_index = boundary_index + 1

        # Handle the last chunk if there are remaining sentences
        if start_index < len(sentences):
            chunk_sentences = sentences[start_index:]
            chunk_text = " ".join(chunk_sentences)
            chunk_document = Document(page_content=chunk_text, metadata=document.metadata.copy())
            chunks.append(chunk_document)

        return chunks