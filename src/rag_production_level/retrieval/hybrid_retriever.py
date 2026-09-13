from langchain_core.documents import Document

from .base_retriever import BaseRetriever
from .vector_retriever import VectorRetriever
from .keyword_retriever import BM25Retriever
from rag_production_level.retrieval.fusion.rrf import ReciprocalRankFusion


class HybridRetriever(BaseRetriever):

    def __init__(
        self,
        vector_retriever: VectorRetriever,
        bm25_retriever: BM25Retriever,
        fusion: ReciprocalRankFusion,
    ):
        self.vector_retriever = vector_retriever
        self.bm25_retriever = bm25_retriever
        self.fusion = fusion

    def retrieve(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:

        vector_results = self.vector_retriever.retrieve(
            query,
            documents,
            top_k=top_k,
        )

        bm25_results = self.bm25_retriever.retrieve(
            query,
            documents,
            top_k=top_k,
        )

        vector_ids = [
            document.metadata["chunk_id"]
            for document in vector_results
        ]

        bm25_ids = [
            document.metadata["chunk_id"]
            for document in bm25_results
        ]

        fused_ids = self.fusion.fuse(
            [vector_ids, bm25_ids],
            top_k=top_k,
        )

        document_lookup = {
            document.metadata["chunk_id"]: document
            for document in documents
        }

        return [
            document_lookup[chunk_id]
            for chunk_id in fused_ids
        ]