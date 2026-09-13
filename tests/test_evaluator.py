from pathlib import Path

from rag_production_level.chunking.recursive_chunker import RecursiveChunker
from rag_production_level.document_Loader.document_loaders import DocumentLoader
from rag_production_level.embeddings.local_embedding import LocalEmbedding
from rag_production_level.evaluation.evaluator import Evaluator
from rag_production_level.retrieval.vector_retriever import VectorRetriever
from rag_production_level.evaluation.metrics import precision_at_k
def test_load_evaluation_data():
    evaluator = Evaluator()
    test_file_path = Path("/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/evaluation/questions.json")
    evaluation_data = evaluator.load_evaluation_data(test_file_path)
    
    assert len(evaluation_data) == 30
    assert evaluation_data[0]["id"]== "Q001"

def test_evaluate_Q001():
    evaluator = Evaluator()
    test_file_path = Path("/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/evaluation/questions.json")
    evaluation_data = evaluator.load_evaluation_data(test_file_path)
    
    evaluation_question = evaluation_data[24]  # Q001

    embedding_model = LocalEmbedding()
    retriever = VectorRetriever(embedding_model)

    # Load the documents to be used for retrieval
    document_loader = DocumentLoader()
    chunker = RecursiveChunker(chunk_size=300, chunk_overlap=50)

    documents = []
    corpus_path = Path("/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/text")

    for file_path in corpus_path.glob("*.txt"):
        loaded_documents = document_loader.load_file(file_path)
        documents.extend(loaded_documents)

    chunked_documents = chunker.chunk(documents)

    result = evaluator.evaluate(evaluation_question, retriever, chunked_documents, k=5)
    print(f"Q001 Evaluation Result: {result}")
    assert result in [0.0,1.0]

def test_evaluate_all():

    evaluator = Evaluator()

    questions_path = Path("/Users/rajnish/Developer/Code/RAG Production Level/src/rag_production_level/Docs/rag_document_corpus/evaluation/questions.json")

    questions = evaluator.load_evaluation_data(questions_path)

    embedding_model = LocalEmbedding()
    retriever = VectorRetriever(embedding_model)

    document_loader = DocumentLoader()
    chunker = RecursiveChunker()

    documents = []

    corpus_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/"
        "src/rag_production_level/Docs/rag_document_corpus"
    )

    supported_extensions = {
    ".pdf",
    ".txt",
    ".md",
    ".cs",
    ".java",
    ".py",
    ".sql",
}

    for file_path in corpus_path.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            documents.extend(document_loader.load_file(file_path))

    chunks = chunker.chunk(documents)

    result = evaluator.evaluate_all(
        questions,
        retriever,
        chunks,
        k=5,
    )

    print(f"\nOverall Recall@5: {result['overall_recall']:.2%}")
    print(f"Overall Precision@5: {result['overall_precision']:.2%}")
    print(f"Overall Reciprocal Rank@5: {result['overall_reciprocal_rank']:.2%}")

    assert 0.0 <= result['overall_recall'] <= 1.0

def test_evaluate_Q025():
    evaluator = Evaluator()

    test_file_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/"
        "src/rag_production_level/Docs/rag_document_corpus/evaluation/questions.json"
    )

    evaluation_data = evaluator.load_evaluation_data(test_file_path)
    evaluation_question = evaluation_data[24]  # Q025

    embedding_model = LocalEmbedding()
    retriever = VectorRetriever(embedding_model)

    document_loader = DocumentLoader()
    chunker = RecursiveChunker()

    documents = []

    corpus_path = Path(
        "/Users/rajnish/Developer/Code/RAG Production Level/"
        "src/rag_production_level/Docs/rag_document_corpus"
    )

    supported_extensions = {
        ".pdf",
        ".txt",
        ".md",
        ".cs",
        ".java",
        ".py",
        ".sql",
    }

    for file_path in corpus_path.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            documents.extend(document_loader.load_file(file_path))

    chunks = chunker.chunk(documents)

    result = evaluator.evaluate(
        evaluation_question,
        retriever,
        chunks,
        k=5,
    )

    print(f"Q025 Evaluation Result: {result}")

    assert result in [0.0, 1.0]

