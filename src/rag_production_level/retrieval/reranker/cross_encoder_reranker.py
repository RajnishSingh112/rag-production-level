from sentence_transformers import CrossEncoder

from langchain_core.documents import Document

from .base_reranker import BaseReranker


class CrossEncoderReranker(BaseReranker):

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):
        self.model_name = model_name
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:

        pairs = [
            (query, document.page_content)
            for document in documents
        ]

        scores = self.model.predict(pairs)

        ranked_documents = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            document
            for document, _ in ranked_documents[:top_k]
        ]