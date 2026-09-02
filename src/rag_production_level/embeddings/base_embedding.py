from abc  import ABC, abstractmethod

class BaseEmbedding(ABC):
    @abstractmethod
    def embed_text(self, query: str) -> list[float]:
        pass