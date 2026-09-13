from langchain_core.documents import Document

from rag_production_level.retrieval.hybrid_retriever import (
    HybridRetriever,
)
from rag_production_level.retrieval.vector_retriever import (
    VectorRetriever,
)
from rag_production_level.retrieval.keyword_retriever import (
    BM25Retriever,
)
from rag_production_level.retrieval.fusion.rrf import (
    ReciprocalRankFusion,
)
from rag_production_level.embeddings.local_embedding import (
    LocalEmbedding,
)


def test_hybrid_retriever():

    documents = [
        Document(
            page_content="MetadataService uses optimistic concurrency.",
            metadata={"chunk_id": "A"},
        ),
        Document(
            page_content="Documents are processed asynchronously.",
            metadata={"chunk_id": "B"},
        ),
        Document(
            page_content="The database uses PostgreSQL.",
            metadata={"chunk_id": "C"},
        ),
    ]

    embedding = LocalEmbedding()

    vector_retriever = VectorRetriever(embedding)

    bm25_retriever = BM25Retriever(documents)

    fusion = ReciprocalRankFusion()

    hybrid = HybridRetriever(
        vector_retriever=vector_retriever,
        bm25_retriever=bm25_retriever,
        fusion=fusion,
    )

    results = hybrid.retrieve(
        "MetadataService optimistic concurrency",
        documents,
        top_k=2,
    )

    assert len(results) == 2

    assert results[0].metadata["chunk_id"] == "A"