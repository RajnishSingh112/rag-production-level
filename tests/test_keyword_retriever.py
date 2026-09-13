from langchain_core.documents import Document

from rag_production_level.retrieval.keyword_retriever import BM25Retriever


def test_bm25_retrieves_keyword_match():

    documents = [
        Document(
            page_content="MetadataService uses optimistic concurrency."
        ),
        Document(
            page_content="Documents are processed asynchronously."
        ),
        Document(
            page_content="The database uses PostgreSQL."
        ),
    ]

    retriever = BM25Retriever(documents)

    results = retriever.retrieve(
        "MetadataService optimistic concurrency",
        top_k=1,
    )

    assert "MetadataService" in results[0].page_content
    