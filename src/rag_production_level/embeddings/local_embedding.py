from sentence_transformers import SentenceTransformer
from .base_embedding import BaseEmbedding

class LocalEmbedding(BaseEmbedding):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(model_name)

    def embed_text(self, query: str) -> list[float]:
        vector = self.embedding_model.encode(query).tolist()
        return vector