from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

from .base_retriever import BaseRetriever


class BM25Retriever(BaseRetriever):

    def __init__(self, documents: list[Document]):
        self.documents = documents

        tokenized_documents = [
            self.tokenize(document.page_content)
            for document in documents
        ]

        self.bm25 = BM25Okapi(tokenized_documents)

    def tokenize(self, text: str) -> list[str]:
        return text.lower().split()

    def retrieve(
        self,
        query: str,
        documents: list[Document] | None = None,
        top_k: int = 5,
    ) -> list[Document]:

        query_tokens = self.tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        ranked_documents = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            document
            for document, _ in ranked_documents[:top_k]
        ]