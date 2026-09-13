from abc import ABC, abstractmethod
from langchain_core.documents import Document


class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str, documents: list[Document], top_k: int=5) -> list[Document]:
        pass