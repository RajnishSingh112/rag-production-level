from langchain_core.documents import Document
from .base_retriever import BaseRetriever
import numpy as np

class VectorRetriever(BaseRetriever):
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def retrieve(self, query: str, documents: list[Document], top_k: int=5) -> list[Document]:
        query_vector = self.embedding_model.embed_text(query)

        stored_documents = []
        for doc in documents:
            document_vector = self.embedding_model.embed_text(doc.page_content)
            similarity = self.cosine_similarity(query_vector, document_vector)
            stored_documents.append((doc, similarity))

        stored_documents.sort(key=lambda x: x[1], reverse=True)
        top_documents = [doc for doc, _ in stored_documents[:top_k]]
        # Return the top_k most similar documents
        return top_documents

    
    def cosine_similarity(self, vec1: list[float], vec2: list[float]) -> float:
        # Calculate the cosine similarity between two vectors
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))