from pathlib import Path
from rag_production_level.Docs.rag_document_corpus.code.python.document_service import Document
from rag_production_level.chunking.recursive_chunker import RecursiveChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader
from rag_production_level.embeddings.local_embedding import LocalEmbedding
from rag_production_level.retrieval.vector_retriever import VectorRetriever
from rag_production_level.retrieval.keyword_retriever import BM25Retriever
from rag_production_level.retrieval.fusion.rrf import ReciprocalRankFusion
from rag_production_level.retrieval.hybrid_retriever import HybridRetriever
from rag_production_level.evaluation.evaluator import Evaluator
from rag_production_level.retrieval.reranker.cross_encoder_reranker import (
    CrossEncoderReranker,
)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

CORPUS_PATH = (
    PROJECT_ROOT
    / "src"
    / "rag_production_level"
    / "Docs"
    / "rag_document_corpus"
)

QUESTIONS_PATH = (
    CORPUS_PATH
    / "evaluation"
    / "questions.json"
)
def load_corpus():
    document_loader = DocumentLoader()

    supported_extensions = {
        ".pdf",
        ".txt",
        ".md",
        ".cs",
        ".java",
        ".py",
        ".sql",
    }

    documents = []

    for file_path in CORPUS_PATH.rglob("*"):
        if (
            file_path.is_file()
            and file_path.suffix.lower() in supported_extensions
        ):
            documents.extend(
                document_loader.load_file(file_path)
            )

    return documents

class RerankedHybridRetriever:

    def __init__(self, hybrid_retriever, reranker):
        self.hybrid_retriever = hybrid_retriever
        self.reranker = reranker

    def retrieve(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:

        candidates = self.hybrid_retriever.retrieve(
            query,
            documents,
            top_k=20,
        )

        return self.reranker.rerank(
            query,
            candidates,
            top_k=top_k,
        )

def main():

    print("Loading corpus...")

    documents = load_corpus()
    evaluator = Evaluator()
    questions = evaluator.load_evaluation_data(QUESTIONS_PATH)
    chunker = RecursiveChunker(chunk_size=300, chunk_overlap=50)
    chunks = chunker.chunk(documents)
    embedding = LocalEmbedding()

    vector_retriever = VectorRetriever(embedding)

    bm25_retriever = BM25Retriever(chunks)

    fusion = ReciprocalRankFusion()

    hybrid_retriever = HybridRetriever(
        vector_retriever=vector_retriever,
        bm25_retriever=bm25_retriever,
        fusion=fusion,
    )
    reranker = CrossEncoderReranker()

    reranked_hybrid = RerankedHybridRetriever(
    hybrid_retriever=hybrid_retriever,
    reranker=reranker,
    )

    result = evaluator.evaluate_all(
        questions,
        reranked_hybrid,
        chunks,
        k=5,
    )

    #print("\n=== HYBRID RESULTS ===")
    #print(f"Recall@5: {result['overall_recall']:.2%}")
    #print(f"Precision@5: {result['overall_precision']:.2%}")
    #print(f"MRR@5: {result['overall_reciprocal_rank']:.2%}")

    print("\n=== HYBRID + RERANKER RESULTS ===")
    print(f"Recall@5: {result['overall_recall']:.2%}")
    print(f"Precision@5: {result['overall_precision']:.2%}")
    print(f"MRR@5: {result['overall_reciprocal_rank']:.2%}")

if __name__ == "__main__":
    main()
