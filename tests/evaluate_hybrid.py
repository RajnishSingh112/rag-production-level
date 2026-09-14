from pathlib import Path
from rag_production_level.chunking.recursive_chunker import RecursiveChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader
from rag_production_level.embeddings.local_embedding import LocalEmbedding
from rag_production_level.retrieval.vector_retriever import VectorRetriever
from rag_production_level.retrieval.keyword_retriever import BM25Retriever
from rag_production_level.retrieval.fusion.rrf import ReciprocalRankFusion
from rag_production_level.retrieval.hybrid_retriever import HybridRetriever
from rag_production_level.evaluation.evaluator import Evaluator

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


    result = evaluator.evaluate_all(
        questions,
        hybrid_retriever,
        chunks,
        k=5,
    )

    print("\n=== HYBRID RESULTS ===")
    print(f"Recall@5: {result['overall_recall']:.2%}")
    print(f"Precision@5: {result['overall_precision']:.2%}")
    print(f"MRR@5: {result['overall_reciprocal_rank']:.2%}")

if __name__ == "__main__":
    main()
